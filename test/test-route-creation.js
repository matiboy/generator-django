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
                ]);
            });
        });
    });
    describe('main urls and namespacing', function() {
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

    describe('app urls', function() {
        beforeEach(function (done) {
            var folder = path.join(__dirname, 'temp');
            helpers.testDirectory(folder, function (err) {
                if (err) {
                    return done(err);
                }

                // Copy fresh test urls to
                // fs.mkdirSync('apps');
                // fs.mkdirSync('apps/accounts');
                fs.copySync(inputUrls, 'urls.py');

                fs.copySync('../input/app_urls.py', 'apps/accounts/urls.py');

                this.app = helpers.createGenerator('django:route', [
                    '../../route'
                ], ['accounts']);
                done();
            }.bind(this));
        });
        it('should create the urls file if it doesn t exist', function(done) {
            helpers.mockPrompt(this.app, {
                url: '^profile/(?P<id>\\d+)$',
                viewClass: 'OtherAccount',
                urlName: 'other_account'
            });
            this.app.run({}, function () {
                var expected = ['apps/accounts/urls.py'];
                done();
            });
        });
        it('should add the correct line into urls.py without login required', function(done) {
            helpers.mockPrompt(this.app, {
                url: '^profile/(?P<id>\\d+)$',
                viewClass: 'OtherAccount',
                urlName: 'other_account'
            });
            this.app.run({}, function () {
                assert.equal(fs.readFileSync('../output/added_url_no_login.py', {encoding:'utf8'}),fs.readFileSync('apps/accounts/urls.py', {encoding:'utf8'}))
                done();
            });
        });
        it('should add the correct line into urls.py with login required', function(done) {
            helpers.mockPrompt(this.app, {
                url: '^profile/(?P<id>\\d+)$',
                viewClass: 'OtherAccount',
                urlName: 'other_account'
            });
            this.app.run({}, function () {
                helpers.mockPrompt(this.app, {
                    url: '^(?P<id>\\d+)$',
                    viewClass: 'MyFinances',
                    urlName: 'my_finances',
                    requiresLogin: true
                });
                this.app.run({}, function () {

                    assert.equal(fs.readFileSync('../output/added_two_urls_one_with_login.py', {encoding:'utf8'}),fs.readFileSync('apps/accounts/urls.py', {encoding:'utf8'}))
                    done();
                });
            }.bind(this));
        });
    });
    describe('view classes', function() {
        beforeEach(function (done) {
            var folder = path.join(__dirname, 'temp');
            helpers.testDirectory(folder, function (err) {
                if (err) {
                    return done(err);
                }

                // Copy fresh test urls to
                // fs.mkdirSync('apps');
                // fs.mkdirSync('apps/accounts');
                fs.copySync(inputUrls, 'urls.py');

                fs.copySync('../input/app_urls.py', 'apps/accounts/urls.py');

                this.app = helpers.createGenerator('django:route', [
                    '../../route'
                ], ['accounts']);
                done();
            }.bind(this));
        });
        it('should create the views file if it doesn t exist', function(done) {
            helpers.mockPrompt(this.app, {
                url: '^profile/(?P<id>\\d+)$',
                viewClass: 'OtherAccount',
                urlName: 'other_account'
            });
            this.app.run({}, function () {
                var expected = ['apps/accounts/views.py'];
                done();
            });
        });
        it('should add the correct view class and corresponding methods into views.py', function(done) {
            helpers.mockPrompt(this.app, {
                url: '^profile/(?P<id>\\d+)$',
                viewClass: 'OtherAccount',
                urlName: 'other_account',
                methods: ['GET', 'POST']
            });
            this.app.run({}, function () {
                assert.equal(fs.readFileSync('../output/views_with_class.py', {encoding:'utf8'}),fs.readFileSync('apps/accounts/views.py', {encoding:'utf8'}))
                done();
            });
        });
    });
});
