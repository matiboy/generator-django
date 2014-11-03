/*global describe, beforeEach, it*/
'use strict';

var path    = require('path');
var helpers = require('yeoman-generator').test;
var fs = require('fs-extra');
var assert = require('assert');

var inputUrls = '../input/main_urls.py';

describe('django route generator', function () {
    describe('required arguments', function() {
        it('throws if no app name', function() {
            assert.throws(function createApp() {
                this.app = helpers.createGenerator('django:route', [
                    '../../route'
                ])
            });
        });
    });
    describe('namespacing', function() {
        beforeEach(function (done) {
            var folder = path.join(__dirname, 'temp');
            helpers.testDirectory(folder, function (err) {
                if (err) {
                    return done(err);
                }

                // Copy fresh test urls to folder
                fs.copySync(inputUrls, 'urls.py');

                this.app = helpers.createGenerator('django:route', [
                    '../../route'
                ], ['harlo']);
                done();
            }.bind(this));
        });

        it('doesnt modify urls.py if app urls are already in', function (done) {
            this.app = helpers.createGenerator('django:route', [
                    '../../route'
                ], ['accounts']);
            helpers.mockPrompt(this.app, {
                'namespace': 'dsa'
            });
            this.app.run({}, function () {
                assert.equal(fs.readFileSync(inputUrls, {encoding:'utf8'}),fs.readFileSync('urls.py', {encoding:'utf8'}))
                done();
            });
        });

        it('adds correct namespace to urls.py', function (done) {
            helpers.mockPrompt(this.app, {
                'namespace': 'blop',
                'subdirectory': 'chicken'
            });
            this.app.run({}, function () {
                assert.equal(fs.readFileSync('../output/added_namespace.py', {encoding:'utf8'}),fs.readFileSync('urls.py', {encoding:'utf8'}))
                done();
            });
        });

        it('adds correct namespace to urls.py with or without subdirectory', function (done) {
            helpers.mockPrompt(this.app, {
                'namespace': 'blop',
                'subdirectory': ''
            });
            this.app.run({}, function () {
                assert.equal(fs.readFileSync('../output/added_namespace_no_subdirectory.py', {encoding:'utf8'}),fs.readFileSync('urls.py', {encoding:'utf8'}))
                done();
            });
        });
    });
});
