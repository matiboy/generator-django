'use strict';
// Dependencies
var util = require('util');
var path = require('path');
var fs = require('fs');
var yeoman = require('yeoman-generator');
var LineByLineReader = require('line-by-line');
var changeCase = require('change-case');


var chalk = require('chalk');

var foldername = path.basename(process.cwd());

// Export generator
var DjangoRouteGenerator = module.exports = function DjangoRouteGenerator(args, options, config) {
  yeoman.generators.Base.apply(this, arguments);
  if(!args[0]) {
    throw 'App name is required';
  }
  this.APPNAME = args[0];
  this.appDir = 'apps/' + args[0];
  this.urlsFile = this.appDir + '/urls.py';
  this.viewsFile = this.appDir + '/views.py';
  this.on('end', function () {
  });

  this.pkg = JSON.parse(this.readFileAsString(path.join(__dirname, '../package.json')));
};

util.inherits(DjangoRouteGenerator, yeoman.generators.Base);

// Create files needed
DjangoRouteGenerator.prototype.createFile = function createFile() {
    if(fs.existsSync(this.urlsFile)){
      this.log(chalk.green('Url file already exists'));
    } else {
      this.template('urls.py', this.urlsFile);
    }
    if(fs.existsSync(this.viewsFile)){
      this.log(chalk.green('Test file already exists'));
    } else {
      this.copy('views.py', this.viewsFile);
    }
}

// Check whether this app's urls have already been added

DjangoRouteGenerator.prototype._urlsExists = function _urlExists(cb) {
    // Open read url file
    var lr = new LineByLineReader('urls.py');
    var term = "'"+this.APPNAME+".urls'";
    var found = false;
    lr.on('line', function(line) {
        if(line.indexOf(term) !== -1) {
            found = true;
            cb(true);
        }
    });
    lr.on('end', function(){
        if(!found) {
            return cb(false);
        }
    });
};

DjangoRouteGenerator.prototype.urls = function urls() {
    var cb = this.async();
    this._urlsExists(function(found) {
        if(!found) {
            this.needsUrls = true;
        } else {
            this.log(chalk.green('App urls already added to main urls'));
        }
        cb();
    }.bind(this));
};

DjangoRouteGenerator.prototype.subdirectory = function subdirectory() {
    var cb = this.async();
    if(this.needsUrls) {
        // prompt for new url sub folder
        this.prompt({
            name: 'subdirectory',
            message: 'Subdirectory',
        }, function(props){
            this.subdirectory = props.subdirectory;
            cb();
        }.bind(this));
    } else {
        cb();
    }
};

DjangoRouteGenerator.prototype._namespaceExists = function _namespaceExists(ns, cb) {
    // Open read url file
    var lr = new LineByLineReader('urls.py');
    var term = "namespace='"+ns+"'";
    var found = false;
    lr.on('line', function(line) {
        if(line.indexOf(term) !== -1) {
            found = true;
            cb(true);
        }
    });
    lr.on('end', function(){
        if(!found){
            return cb(false);
        }
    });
};

DjangoRouteGenerator.prototype.namespace = function namespace() {
    var cb = this.async();
    if(this.needsUrls) {
        var prompts = [{
            name: 'namespace',
            message: 'Namespace [leaving blank means no namespace]'
          }];
      this.prompt(prompts, function(props) {
        // If namespace, check if new
        this.namespace = props.namespace;
        if(props.namespace) {
            this._namespaceExists(props.namespace, function gotNamespace(found) {
                if(found) {
                    this.log(chalk.yellow('Namespace already exists'));
                }
                cb();
            }.bind(this));
        } else {
            cb();
        }
      }.bind(this));

    } else {
        cb();
    }
};

DjangoRouteGenerator.prototype.writeurls = function writeurls() {
    var cb = this.async();

    if(this.needsUrls) {
        // Prepare the line
        var line = "    url(r'<%= subdir %>', include('<%= appName %>.urls', namespace='<%= ns %>')),";
        line = this._.template(line, {
            subdir: this.subdirectory ? '^' + this.subdirectory + '/' : '',
            ns: this.namespace,
            appName: this.APPNAME
        });
        // Find right place
        var content = this.readFileAsString('urls.py');
        var patterns = content.indexOf('patterns(');
        var nextComma = content.indexOf(',', patterns) + 1;
        var newContent = (content.slice(0,nextComma) + '\n' + line + content.slice(nextComma));
        this.writeFileFromString(newContent, 'urls.py');

    }
    cb();
};

DjangoRouteGenerator.prototype.routeDetails = function routeDetails() {
    var cb = this.async();
    var prompts = [
        {
            name: 'url',
            message: 'Url pattern'
            // Good idea but doesn't work
            // type: 'rawlist',
            // choices: [
            //     "''",
            //     "r'^(?P<id>\d+)$'",
            //     "r'^(?P<id>\d+)/(?P<slug>[\w\d-]+)$'",
            // ]
        },
        {
            name: 'viewClass',
            message: 'View class'
        },
        {
            name: 'urlName',
            message: 'Url name',
            default: function(props) {
                return changeCase.snakeCase(props.viewClass);
            }
        },
        {
            name: 'methods',
            type: 'checkbox',
            choices: ['GET', 'POST', 'DELETE', 'PUT'],
            message: 'Methods'
        },
        {
            name: 'requiresLogin',
            message: 'Requires login?',
            type: 'confirm',
            default: false
        }
    ];

    this.prompt(prompts, function(props) {
        this.url = props.url;
        this.methods = props.methods;
        this.requiresLogin = props.requiresLogin;
        this.viewClass = props.viewClass;
        this.urlName = props.urlName;
        cb();
    }.bind(this));
};

DjangoRouteGenerator.prototype.writeUrl = function writeUrl() {
    if(this.requiresLogin) {
        var subline = "login_required(views.<%= viewClass %>.as_view())";
    } else {
        var subline = "views.<%= viewClass %>.as_view()";
    }
    var line = "    url(r'<%= url %>', " + subline + ", name='<%= urlName %>'),";
    line = this._.template(line, this);
    // Find right place
    var content = this.readFileAsString(this.urlsFile);
    var patterns = content.indexOf('patterns(');
    var nextComma = content.indexOf(',', patterns) + 1;
    var newContent = (content.slice(0,nextComma) + '\n' + line + content.slice(nextComma));
    this.writeFileFromString(newContent, this.urlsFile);
};

DjangoRouteGenerator.prototype.writeViews = function writeViews() {
    // Find right place
    var content = this.readFileAsString(this.viewsFile);
    var fileContent = this.src.read('_viewClass.js');
    var compiled = this.engine(fileContent, this);
    var newContent = content + compiled;
    this.writeFileFromString(newContent, this.viewsFile);
};
