<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Introduction](#introduction)
- [Create a project structure by using yeoman](#create-a-project-structure-by-using-yeoman)
  - [Step1: Set up your dev environment](#step1-set-up-your-dev-environment)
    - [Install prerequisites](#install-prerequisites)
    - [Install the Yeoman toolset](#install-the-yeoman-toolset)
    - [Confirm installation](#confirm-installation)
  - [Step2: Install a Yeoman generator](#step2-install-a-yeoman-generator)
    - [Install an AngularJS generator](#install-an-angularjs-generator)
  - [Step3: Use a generator to scaffold out your app](#step3-use-a-generator-to-scaffold-out-your-app)
    - [Create a project folder](#create-a-project-folder)
    - [Access generators via the Yeoman menu](#access-generators-via-the-yeoman-menu)
    - [Generate the project structure](#generate-the-project-structure)
  - [Step4: Review the Yeoman-generated app](#step4-review-the-yeoman-generated-app)
  - [Step5: Preview your app in the browser](#step5-preview-your-app-in-the-browser)
    - [Start the server](#start-the-server)
    - [Stop the server](#stop-the-server)
    - [Watch your files](#watch-your-files)
- [Issues & Solutions](#issues-&-solutions)
  - [issue1: Cannot find where you keep your Bower packages](#issue1-cannot-find-where-you-keep-your-bower-packages)
  - [issue2: Cannot find module 'karma'](#issue2-cannot-find-module-karma)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introduction

This document introduces the usage of yeoman.

In a traditional web development workflow, you would need to spend a lot of time setting up boilerplate code for your webapp, downloading dependencies, and manually creating your web folder structure. Yeoman generators can be the rescue. When We create a new project, we can use yeoman to quickly create a project structure with just a command or two. 

## Create a project structure by using yeoman

There we will use yeoman to create a web application for angularjs project.

### Step1: Set up your dev environment

Most of your interactions with Yeoman will be through the command line, run commands in the terminal app if you are on Mac.

#### Install prerequisites

Before installing Yeoman, you will need the following:
	- Node.js v0.10.x+
	- npm(which comes bundled with Node) v2.1.0+
	- git
	
You can check if you have Node and npm installed by issuing the following command:

```
$ node --version && npm --version
```

If you need to upgrade or install Node, the easiest way is to use an installer for your platform. Download ".pkg" for Mac from the [NodeJs website](https://nodejs.org/download/)
The [npm](https://www.npmjs.com/) package manager is bundled with Node, although you might need to update it. Some Node versions ship with rather old versions of npm. You can update npm using this command:

```
$ npm install --global npm@latest
```

You can check if you have Git installed by issuing the following command:

```
$ git --version
```
If you don't have Git, grab the installers from the [git website](http://git-scm.com/)

#### Install the Yeoman toolset

Once you have got Node installed, install the Yeoman toolset:

```
$ npm install --global yo bower grunt-cli
```

#### Confirm installation

It is a good idea to check that everything is installed as expected by running commonly used Yeoman commands like yo,bower and grunt with the --version flag as follows:

```
$ yo --version && bower --version && grunt --version
```
Running the above should output three seperate version numbers:
	- Yeoman
	- Bower
	- Grunt CLI(the command-line interface for Grunt)

### Step2: Install a Yeoman generator

 Let's install a generator for AngularJS projects.

#### Install an AngularJS generator

You can install Yeoman generators using the npm command, install generator-angular and generator-karma using this command:

```
$ sudo npm install --global generator-angular@0.11.1 generator-karma
```
This will start to install the Node packages required for the generator. 

### Step3: Use a generator to scaffold out your app

#### Create a project folder

Create a mytodo folder for all your codelab work:

```
$ mkdir mytodo && cd mytodo
```
This folder is where the generator will place your scaffolded project files.

#### Access generators via the Yeoman menu

Run yo to see your generators:

```
$ yo
``` 
like this:
![yo demo](/awesome5team/General-Resources-Box/blob/master/assets/images/yo-demo.png?raw=true = 50x100)
If you have a few generators installed, you will be able to interactively choose from them, highlight "Angular", hit enter to run the generator.

#### Generate the project structure

After runing the yo command, you can look at this:![yo angular](https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png=100x50)

and it has provided the optional settings to customize your app with common developer libraries to speed up the initial setup of your development environment. Here you can choose whether use Sass, Bootstrap:![use Sass and Bootstrap or not](/awesome5team/General-Resources-Box/blob/master/assets/images/use-Sass-and-Bootstrap-or-not.png?raw=true)

Then you can choose the modules which need to be contained in your project folder, hint "enter" to build project directory.
 ![choose module](/awesome5team/General-Resources-Box/blob/master/assets/images/choose-modules.png?raw=true)


After runing finished, you will look at this:
![run successfully](/awesome5team/General-Resources-Box/blob/master/assets/images/run-successfully.png?raw=true)



### Step4: Review the Yeoman-generated app

In mytodo folder, we have:

app: a parent directory for our web application

- index.html: the base html file for our Angular app
- 404.html, favicon.ico, and robots.txt: commonly used web files so you don't have to create them yourself
	- scripts: our own JS files
		- app.js: our main Angular application code
		- controllers: our Angular controllers
	- styles: our CSS files
	- views: a place for our Angular templates
	
bower_components, bower.json: our JavaScript/web dependencies, installed by Bower
	
Gruntfile.js,package.json and node_modules: configuration and dependencies required by our Grunt tasks

test: a scaffolded out test runner and the unit tests for the project, including boilerplate tests for our controllers.


### Step5: Preview your app in the browser

To preview your web app in your favourite web browser, you don't have to do anything special to set up a local web server on your computer.

#### Start the server

Run a Grunt task to create a local, Node-based http server on [localhost:9000](http://localhost:9000/) or [127.0.0.1:9000](http://127.0.0.1:9000/) for some configurations by issuing the following command:

```
$ grunt serve
``` 
Your web browser will launch your newly scaffolded application in a new tab.


#### Stop the server

If you ever need to stop the server, use "Ctrl+C" keyboard command to quit your current CLI process.


#### Watch your files

Open up your favourite text editor and start making changes. Each save will automatically force a browser refresh so you don't have to do this yourself.

Then you can write your code based on this folder.

## Issues & Solutions

### issue1: Cannot find where you keep your Bower packages
Here you maybe encounter such a issue:

```
Running "wiredep:app" (wiredep) task
Warning: Error: Cannot find where you keep your Bower packages. Use --force to continue.
```

the solution for this issue is that create a folder named bower_components in the project folder, then run the following command:

```
 $ rm -rf ~/.bower
 $ sudo npm install -g bower
 $ bower install
```

after executing the command of "bower install", you may encounter such issue:

```
ERROR: EACCES: permission denied, open '/Users/appledev083/.config/configstore/insight-bower.json'
```
You may fixed this question by issuing the following command:

```
$ cd /Users/appledev083/.config/configstore/
$ chmod 777 insight-bower.json
```
Here you maybe encounter another issue:

```
fatal: unable to connect to github.com: github.com[0: 192.30.252.130]: errno=Connection refused
```

You can fixed this question by connecting the private VPN in your computer. 

### issue2: Cannot find module 'karma'

You also may encounter such issue: ![error2](/awesome5team/General-Resources-Box/blob/master/assets/images/karma-error.png?raw=true)

the solution for this issue is that you need to install phanatomjs, jasmine-core, karma and grunt-karma:

```
$ sudo npm install phantomjs@1.9
$ sudo npm install jasmine-core@*
$ sudo npm install karma
$ sudo npm install grunt-karma
```

## References

- [Meet Yeoman](http://yeoman.io/codelab/meet-yeoman.html)
- [karma error](http://stackoverflow.com/questions/19203051/cannot-find-module-karma-while-using-grunt)