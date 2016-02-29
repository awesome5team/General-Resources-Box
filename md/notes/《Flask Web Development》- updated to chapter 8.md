<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [前言](#%E5%89%8D%E8%A8%80)
  - [Flask框架的特点](#flask%E6%A1%86%E6%9E%B6%E7%9A%84%E7%89%B9%E7%82%B9)
  - [本书的组织方式](#%E6%9C%AC%E4%B9%A6%E7%9A%84%E7%BB%84%E7%BB%87%E6%96%B9%E5%BC%8F)
  - [本书面向的读者](#%E6%9C%AC%E4%B9%A6%E9%9D%A2%E5%90%91%E7%9A%84%E8%AF%BB%E8%80%85)
  - [本书的主体结构](#%E6%9C%AC%E4%B9%A6%E7%9A%84%E4%B8%BB%E4%BD%93%E7%BB%93%E6%9E%84)
  - [如何使用本书的示例代码](#%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E6%9C%AC%E4%B9%A6%E7%9A%84%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81)
    - [获取和检出代码](#%E8%8E%B7%E5%8F%96%E5%92%8C%E6%A3%80%E5%87%BA%E4%BB%A3%E7%A0%81)
    - [安装数据库和packages](#%E5%AE%89%E8%A3%85%E6%95%B0%E6%8D%AE%E5%BA%93%E5%92%8Cpackages)
    - [会用到的Git操作](#%E4%BC%9A%E7%94%A8%E5%88%B0%E7%9A%84git%E6%93%8D%E4%BD%9C)
- [第1章 Flask框架的安装和配置](#%E7%AC%AC1%E7%AB%A0-flask%E6%A1%86%E6%9E%B6%E7%9A%84%E5%AE%89%E8%A3%85%E5%92%8C%E9%85%8D%E7%BD%AE)
  - [轻吹Flask](#%E8%BD%BB%E5%90%B9flask)
  - [创建和激活虚拟环境](#%E5%88%9B%E5%BB%BA%E5%92%8C%E6%BF%80%E6%B4%BB%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83)
  - [在虚拟环境下来安装Flask](#%E5%9C%A8%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%E4%B8%8B%E6%9D%A5%E5%AE%89%E8%A3%85flask)
- [第2章 Flask应用的基本结构](#%E7%AC%AC2%E7%AB%A0-flask%E5%BA%94%E7%94%A8%E7%9A%84%E5%9F%BA%E6%9C%AC%E7%BB%93%E6%9E%84)
  - [Flask应用的各个部分](#flask%E5%BA%94%E7%94%A8%E7%9A%84%E5%90%84%E4%B8%AA%E9%83%A8%E5%88%86)
    - [初始化应用示例](#%E5%88%9D%E5%A7%8B%E5%8C%96%E5%BA%94%E7%94%A8%E7%A4%BA%E4%BE%8B)
    - [路由和视图函数](#%E8%B7%AF%E7%94%B1%E5%92%8C%E8%A7%86%E5%9B%BE%E5%87%BD%E6%95%B0)
    - [启动Server](#%E5%90%AF%E5%8A%A8server)
  - [完整的示例代码](#%E5%AE%8C%E6%95%B4%E7%9A%84%E7%A4%BA%E4%BE%8B%E4%BB%A3%E7%A0%81)
  - [请求-响应的生命周期](#%E8%AF%B7%E6%B1%82-%E5%93%8D%E5%BA%94%E7%9A%84%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F)
    - [应用与请求的上下文](#%E5%BA%94%E7%94%A8%E4%B8%8E%E8%AF%B7%E6%B1%82%E7%9A%84%E4%B8%8A%E4%B8%8B%E6%96%87)
    - [请求和试图方法的匹配](#%E8%AF%B7%E6%B1%82%E5%92%8C%E8%AF%95%E5%9B%BE%E6%96%B9%E6%B3%95%E7%9A%84%E5%8C%B9%E9%85%8D)
    - [钩子函数](#%E9%92%A9%E5%AD%90%E5%87%BD%E6%95%B0)
    - [响应结果](#%E5%93%8D%E5%BA%94%E7%BB%93%E6%9E%9C)
      - [给返回字符串带状态码](#%E7%BB%99%E8%BF%94%E5%9B%9E%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%B8%A6%E7%8A%B6%E6%80%81%E7%A0%81)
      - [显式使用response](#%E6%98%BE%E5%BC%8F%E4%BD%BF%E7%94%A8response)
      - [redirect](#redirect)
      - [abort](#abort)
  - [如何集成Flask的扩展](#%E5%A6%82%E4%BD%95%E9%9B%86%E6%88%90flask%E7%9A%84%E6%89%A9%E5%B1%95)
    - [带命令行选项的Flask-Script](#%E5%B8%A6%E5%91%BD%E4%BB%A4%E8%A1%8C%E9%80%89%E9%A1%B9%E7%9A%84flask-script)
- [第3章 模板](#%E7%AC%AC3%E7%AB%A0-%E6%A8%A1%E6%9D%BF)
  - [Jinjia2模板引擎](#jinjia2%E6%A8%A1%E6%9D%BF%E5%BC%95%E6%93%8E)
    - [渲染模板](#%E6%B8%B2%E6%9F%93%E6%A8%A1%E6%9D%BF)
    - [变量类型](#%E5%8F%98%E9%87%8F%E7%B1%BB%E5%9E%8B)
    - [控制结构](#%E6%8E%A7%E5%88%B6%E7%BB%93%E6%9E%84)
      - [if else](#if-else)
      - [for](#for)
      - [macro](#macro)
      - [外部导入Macro](#%E5%A4%96%E9%83%A8%E5%AF%BC%E5%85%A5macro)
      - [模板继承](#%E6%A8%A1%E6%9D%BF%E7%BB%A7%E6%89%BF)
  - [Jinjia2集成Bootstrap](#jinjia2%E9%9B%86%E6%88%90bootstrap)
    - [第一步，安装flask-bootstrap](#%E7%AC%AC%E4%B8%80%E6%AD%A5%EF%BC%8C%E5%AE%89%E8%A3%85flask-bootstrap)
    - [第二步，导入flask-bootstrap](#%E7%AC%AC%E4%BA%8C%E6%AD%A5%EF%BC%8C%E5%AF%BC%E5%85%A5flask-bootstrap)
    - [第三步，构建模板覆写父模板](#%E7%AC%AC%E4%B8%89%E6%AD%A5%EF%BC%8C%E6%9E%84%E5%BB%BA%E6%A8%A1%E6%9D%BF%E8%A6%86%E5%86%99%E7%88%B6%E6%A8%A1%E6%9D%BF)
  - [定制错误页面](#%E5%AE%9A%E5%88%B6%E9%94%99%E8%AF%AF%E9%A1%B5%E9%9D%A2)
- [Not Found](#not-found)
  - [用url_for来获得路由地址](#%E7%94%A8url_for%E6%9D%A5%E8%8E%B7%E5%BE%97%E8%B7%AF%E7%94%B1%E5%9C%B0%E5%9D%80)
  - [静态文件](#%E9%9D%99%E6%80%81%E6%96%87%E4%BB%B6)
  - [使用Flask-Moment来格式化时间和日期](#%E4%BD%BF%E7%94%A8flask-moment%E6%9D%A5%E6%A0%BC%E5%BC%8F%E5%8C%96%E6%97%B6%E9%97%B4%E5%92%8C%E6%97%A5%E6%9C%9F)
- [第4章 表单](#%E7%AC%AC4%E7%AB%A0-%E8%A1%A8%E5%8D%95)
  - [跨站点伪装请求(CSRF) 保护](#%E8%B7%A8%E7%AB%99%E7%82%B9%E4%BC%AA%E8%A3%85%E8%AF%B7%E6%B1%82csrf-%E4%BF%9D%E6%8A%A4)
  - [表单类和表单属性](#%E8%A1%A8%E5%8D%95%E7%B1%BB%E5%92%8C%E8%A1%A8%E5%8D%95%E5%B1%9E%E6%80%A7)
  - [在HTML中渲染表单对象](#%E5%9C%A8html%E4%B8%AD%E6%B8%B2%E6%9F%93%E8%A1%A8%E5%8D%95%E5%AF%B9%E8%B1%A1)
  - [表单响应](#%E8%A1%A8%E5%8D%95%E5%93%8D%E5%BA%94)
  - [重定向和用户Session](#%E9%87%8D%E5%AE%9A%E5%90%91%E5%92%8C%E7%94%A8%E6%88%B7session)
  - [消息提示](#%E6%B6%88%E6%81%AF%E6%8F%90%E7%A4%BA)
- [第5章 数据库](#%E7%AC%AC5%E7%AB%A0-%E6%95%B0%E6%8D%AE%E5%BA%93)
  - [数据库简介](#%E6%95%B0%E6%8D%AE%E5%BA%93%E7%AE%80%E4%BB%8B)
    - [SQL数据库](#sql%E6%95%B0%E6%8D%AE%E5%BA%93)
    - [NoSQL数据库](#nosql%E6%95%B0%E6%8D%AE%E5%BA%93)
    - [选择SQL还是NoSQL数据库](#%E9%80%89%E6%8B%A9sql%E8%BF%98%E6%98%AFnosql%E6%95%B0%E6%8D%AE%E5%BA%93)
  - [Python数据库工具选择](#python%E6%95%B0%E6%8D%AE%E5%BA%93%E5%B7%A5%E5%85%B7%E9%80%89%E6%8B%A9)
    - [易用性](#%E6%98%93%E7%94%A8%E6%80%A7)
    - [性能](#%E6%80%A7%E8%83%BD)
    - [可移植性](#%E5%8F%AF%E7%A7%BB%E6%A4%8D%E6%80%A7)
    - [和Flask集成](#%E5%92%8Cflask%E9%9B%86%E6%88%90)
  - [使用Flask-SQLAlchemy进行数据库管理](#%E4%BD%BF%E7%94%A8flask-sqlalchemy%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%BA%93%E7%AE%A1%E7%90%86)
    - [Model定义](#model%E5%AE%9A%E4%B9%89)
    - [关系](#%E5%85%B3%E7%B3%BB)
    - [数据库操作](#%E6%95%B0%E6%8D%AE%E5%BA%93%E6%93%8D%E4%BD%9C)
      - [创建表格](#%E5%88%9B%E5%BB%BA%E8%A1%A8%E6%A0%BC)
      - [插入数据行](#%E6%8F%92%E5%85%A5%E6%95%B0%E6%8D%AE%E8%A1%8C)
      - [修改数据行](#%E4%BF%AE%E6%94%B9%E6%95%B0%E6%8D%AE%E8%A1%8C)
      - [删除数据行](#%E5%88%A0%E9%99%A4%E6%95%B0%E6%8D%AE%E8%A1%8C)
      - [查询数据行](#%E6%9F%A5%E8%AF%A2%E6%95%B0%E6%8D%AE%E8%A1%8C)
    - [在视图方法中操作数据库](#%E5%9C%A8%E8%A7%86%E5%9B%BE%E6%96%B9%E6%B3%95%E4%B8%AD%E6%93%8D%E4%BD%9C%E6%95%B0%E6%8D%AE%E5%BA%93)
    - [Model集成Python Shell](#model%E9%9B%86%E6%88%90python-shell)
    - [使用Flask-Migrate来做数据库的Migrations](#%E4%BD%BF%E7%94%A8flask-migrate%E6%9D%A5%E5%81%9A%E6%95%B0%E6%8D%AE%E5%BA%93%E7%9A%84migrations)
      - [创建迁移的资源库](#%E5%88%9B%E5%BB%BA%E8%BF%81%E7%A7%BB%E7%9A%84%E8%B5%84%E6%BA%90%E5%BA%93)
      - [创建迁移脚本](#%E5%88%9B%E5%BB%BA%E8%BF%81%E7%A7%BB%E8%84%9A%E6%9C%AC)
      - [Upgrading数据库](#upgrading%E6%95%B0%E6%8D%AE%E5%BA%93)
- [第6章 邮件](#%E7%AC%AC6%E7%AB%A0-%E9%82%AE%E4%BB%B6)
  - [Flask-Mail的使用](#flask-mail%E7%9A%84%E4%BD%BF%E7%94%A8)
    - [通过Python Shell发送邮件](#%E9%80%9A%E8%BF%87python-shell%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6)
    - [邮件和应用程序集成](#%E9%82%AE%E4%BB%B6%E5%92%8C%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E9%9B%86%E6%88%90)
    - [发送异步邮件](#%E5%8F%91%E9%80%81%E5%BC%82%E6%AD%A5%E9%82%AE%E4%BB%B6)
- [第7章 大型应用程序架构](#%E7%AC%AC7%E7%AB%A0-%E5%A4%A7%E5%9E%8B%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E6%9E%B6%E6%9E%84)
  - [项目结构](#%E9%A1%B9%E7%9B%AE%E7%BB%93%E6%9E%84)
  - [配置选项](#%E9%85%8D%E7%BD%AE%E9%80%89%E9%A1%B9)
  - [应用程序包App](#%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%8C%85app)
    - [使用工厂方法来构建应用示例](#%E4%BD%BF%E7%94%A8%E5%B7%A5%E5%8E%82%E6%96%B9%E6%B3%95%E6%9D%A5%E6%9E%84%E5%BB%BA%E5%BA%94%E7%94%A8%E7%A4%BA%E4%BE%8B)
    - [使用Blueprint来实现应用程实例的功能](#%E4%BD%BF%E7%94%A8blueprint%E6%9D%A5%E5%AE%9E%E7%8E%B0%E5%BA%94%E7%94%A8%E7%A8%8B%E5%AE%9E%E4%BE%8B%E7%9A%84%E5%8A%9F%E8%83%BD)
  - [启动脚本](#%E5%90%AF%E5%8A%A8%E8%84%9A%E6%9C%AC)
  - [Requirements文件](#requirements%E6%96%87%E4%BB%B6)
  - [单元测试](#%E5%8D%95%E5%85%83%E6%B5%8B%E8%AF%95)
  - [数据库设置](#%E6%95%B0%E6%8D%AE%E5%BA%93%E8%AE%BE%E7%BD%AE)
- [第8章 用户授权](#%E7%AC%AC8%E7%AB%A0-%E7%94%A8%E6%88%B7%E6%8E%88%E6%9D%83)
  - [Flask中授权相关的包和扩展](#flask%E4%B8%AD%E6%8E%88%E6%9D%83%E7%9B%B8%E5%85%B3%E7%9A%84%E5%8C%85%E5%92%8C%E6%89%A9%E5%B1%95)
- [Login](#login)
  - [密码安全](#%E5%AF%86%E7%A0%81%E5%AE%89%E5%85%A8)
    - [使用Werkzeug做密码加密](#%E4%BD%BF%E7%94%A8werkzeug%E5%81%9A%E5%AF%86%E7%A0%81%E5%8A%A0%E5%AF%86)
  - [创建授权的Blueprint](#%E5%88%9B%E5%BB%BA%E6%8E%88%E6%9D%83%E7%9A%84blueprint)
  - [使用Flask-Login来进行用户授权](#%E4%BD%BF%E7%94%A8flask-login%E6%9D%A5%E8%BF%9B%E8%A1%8C%E7%94%A8%E6%88%B7%E6%8E%88%E6%9D%83)
    - [构建登陆的User Model](#%E6%9E%84%E5%BB%BA%E7%99%BB%E9%99%86%E7%9A%84user-model)
    - [保护路由](#%E4%BF%9D%E6%8A%A4%E8%B7%AF%E7%94%B1)
    - [添加登陆表单](#%E6%B7%BB%E5%8A%A0%E7%99%BB%E9%99%86%E8%A1%A8%E5%8D%95)
    - [用户登入](#%E7%94%A8%E6%88%B7%E7%99%BB%E5%85%A5)
    - [用户登出](#%E7%94%A8%E6%88%B7%E7%99%BB%E5%87%BA)
    - [测试登陆功能](#%E6%B5%8B%E8%AF%95%E7%99%BB%E9%99%86%E5%8A%9F%E8%83%BD)
  - [新用户注册](#%E6%96%B0%E7%94%A8%E6%88%B7%E6%B3%A8%E5%86%8C)
    - [添加注册表单](#%E6%B7%BB%E5%8A%A0%E6%B3%A8%E5%86%8C%E8%A1%A8%E5%8D%95)
    - [注册新用户](#%E6%B3%A8%E5%86%8C%E6%96%B0%E7%94%A8%E6%88%B7)
  - [账号确认](#%E8%B4%A6%E5%8F%B7%E7%A1%AE%E8%AE%A4)
    - [使用itsdangerous来初始化确认的token](#%E4%BD%BF%E7%94%A8itsdangerous%E6%9D%A5%E5%88%9D%E5%A7%8B%E5%8C%96%E7%A1%AE%E8%AE%A4%E7%9A%84token)
    - [发送确认的Email](#%E5%8F%91%E9%80%81%E7%A1%AE%E8%AE%A4%E7%9A%84email)
  - [账号管理](#%E8%B4%A6%E5%8F%B7%E7%AE%A1%E7%90%86)
    - [密码修改](#%E5%AF%86%E7%A0%81%E4%BF%AE%E6%94%B9)
    - [密码重置](#%E5%AF%86%E7%A0%81%E9%87%8D%E7%BD%AE)
    - [修改邮箱](#%E4%BF%AE%E6%94%B9%E9%82%AE%E7%AE%B1)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


注：简书并不提供生成目录的功能，笔记多了很不好翻阅，于是代码手动生成了一个简陋的目录。正在考虑自己搭建一个博客，争取在一周内把笔记都迁移到博客上去。 - 2015/07/08

# 前言

## Flask框架的特点

- 其他框架

    大型框架替你做了很多事，同时也限定了你处理问题的方式，比如你只能用一些指定的数据库引擎或者用户授权的方法，要采用其他实现方式会遇到很大的困难。

- Flask框架

    Flask框架被设计成易于扩展的形式，除了一个强壮的内核，基本上所有的功能都要用第三方的扩展来实现。比如数据库，你可以选择NoSQL数据库、可以选择自己开发的数据库，甚至不用数据库。其他的扩展也是如此，你可以任意选择或者自己开发。

    `注`：上述说的Flask的好处，你也从另一个方面来理解，使用大型框架比如Django来做一些快速的开发、常规的解决方案会很方便，而使用Flask意味着什么你都要自己去挑选，这对于开发经验尚且欠缺的人来说是个灾难。


## 本书的组织方式

本书展现了使用Flask开发一个Web应用的流程，当然这只是作者推荐的一种方式。

其他的教材通常是把相关的示例程序提供给你，然后要你自己你集成在一起。本书作者采用了一种不同的方式，本书从一个小例子开始介绍用Flask开发涉及的知识，然后逐渐把它扩展成一个功能完善的博客社交应用。

## 本书面向的读者

- 你应该具有一些Python的编码经验

    虽然本书不要求有Flask开发经验，但是很多Python概念会被涉及，比如：包、模块、方法、decorators和面向对象编程。此外，如果熟悉异常、知道如何从stack traces进行错误诊断也会非常有助于学习。`注：`如果对于本书的示例项目中包的组织方式或者类方法调用不能理解，最好还是学习一些Python知识再往下走，否则容易迷糊。

- 你最好知道基本的命令行操作

    因为本书很多操作都是在命令行进行的，你最好熟悉基本的像定位到文件夹、执行文件、切入到python shell输入Python脚本，以及使用一些Git的clone和check的操作。

- 你最好具备基础的前端知识，

    Web应用免不了使用到前端的几项技术，包括HTML、CSS和JavaScript，书中会直接使用它们而不会再详细介绍。

- 强烈建议你通过克隆项目的方式来学习

    作者把项目发布到了Github上，你可以下载ZIP或TAR包，但是更合理的做法是安装Git客户端到电脑上，然后熟悉基本的Git版本控制的知识。如果你还没接触过Git，强烈推荐你把它作为一个接触和学习Git的机会，后面会有一小节大致介绍如何结合Git使用示例代码。

- 本书不能告诉你所有Flask开发的知识

    本书尽管涉及到了大多数Flask框架的的特性，但你应该把[Official Flask Documentation](http://flask.pocoo.org/) 作为本书的一个补充。


## 本书的主体结构

- 第一部分，介绍Flask
    - 第1章 Flask框架的安装和配置
    - 第2章 Flask应用程序的基本结构
    - 第3章 模板
- 第二部分，一个社交博客应用的构建
- 第三部分，你需要知道的其他知识

## 如何使用本书的示例代码


### 获取和检出代码


本书的示例代码可以从 [https:// github.com/miguelgrinberg/flasky](https:// github.com/miguelgrinberg/flasky)上获取到。

安装好Git客户端以后（如果还没有你可以从[http://git-scm.com](http://git-scm.com)下载），我们就可以通过如下命令导出项目代码了：

```
$ git clone https://github.com/miguelgrinberg/flasky.git
```

如上命令克隆的不只是一份代码，同时也包含了该项目所有的提交记录。所有的代码的提交都有一个tag，并且在这个项目中所有的tag跟章节的顺序是一致的，比如第一章的提交tag是1a, 第五章因为有多次提交所以tag依次是5a、5b等。我们推荐的做法是，导出最老版本的代码进行学习，然后随着学习的推进，切换新版本的代码。如下是一个开始：

```
$ git checkout 1a
```

### 安装数据库和packages

因为检出的项目中只是包含代码，数据库还有一些依赖的库你可能需要单独安装，不过不用担心，执行时候如果未安装会有提示给到我们。

### 会用到的Git操作

如果了解过Git的基础知识就会知道，我们使用 git checkout 命令的时候，本地目录应该是干净的（没有改动过后未提交的代码）。开发过程中难免会想改一改代码，但是要 checkout 到下一个历史节点的时候记得把你的改动给撤销掉，最简单的做法是使用 git reset 命令：

```
$ git reset --hard
```

另外，本书的示例项目flasky的开发者可能因为修复一些bug或者别的原因会改动代码，如果你需要获取到最新的代码以及相应的标签等，你可以执行如下命令来把Github上所有的改动同步过来并覆盖到本地代码（实际上没有太多必要，因为我们知道本书既然出版了作者不大可能把例子改得不利于读者阅读）：

```
$ git fetch --all
$ git fetch --tags
$ git reset --hard origin/master
```

一个对学习有帮助的操作是代码比较，你可以使用命令行来比对两次提交之前哪些代码发生了改变：

```
$ git diff  2a 2b
```

但是在命令行进行代码的比对可读性不好，你可以直接到Github上查看每次提交的改动，比如2a和2b两次提交的差别可以在这里看到：[ https://github.com/miguelgrin berg/flasky/compare/2a...2b]( https://github.com/miguelgrin berg/flasky/compare/2a...2b) 。

# 第1章 Flask框架的安装和配置

## 轻吹Flask

Flask框架很小，但强壮的内核加上丰富的扩展几乎能满足你所有需求。Flask有两个主要的依赖库：Werkzeug和Jinja2，它们都是由Flask核心的开发人员开发的。与其他大型框架不同的是，Flask自身不支持数据库、表单验证、用户授权等复杂的任务，而需要集成其他的扩展，作为一个开发者你需要挑选最合适你项目的扩展。

安装Flask之前你需要安装Python，为了更好的和本书保持一致推荐使用v2.7或者v3.3。


## 创建和激活虚拟环境

安装Flask的最好的办法是在虚拟环境中进行安装，虚拟环境拥有私有的Python编译器，它和其他项目的环境彼此独立，最重要的是它不会污染全局环境。

可以考虑使用第三方套件virtualenv来安装虚拟环境，Mac OS下可以用如下命令来查看是否安装过virtualenv，如果执行下述命令报错了，那么请先安装virtualenv。`注：`该笔记的所有命令行操作都是在Mac OS上的，后面不再重复进行说明。

```
$ virtualenv --version
```

假如安装过easy_install，可以使用easy_install命令安装virtualenv，否则要先安装easy_install（此处不记录安装细节，遇到问题可以参考该书对应的部分）：

```
$ sudo easy_install virtualenv
```

前言部分有介绍如何将项目克隆到本地，下面进入到项目文件夹并构建虚拟环境（环境名为venv，可自定义）：

```
$ cd flasky
$ virtualenv venv
New python executable in venv/bin/python
Installing setuptools, pip...done.
```

激活虚拟环境（编译器路径被暂时加入到了PATH中）：

```
$ source venv/bin/activate
```

激活只是对当前的console窗口有效，可以发现激活以后，命令行头部多了 (venv)。取消激活可以执行如下命令：

```
$ source venv/bin/deactivate
```

## 在虚拟环境下来安装Flask

Python的多数包（包含Flask）都可以用pip进行安装，因为安装virtualenv的过程已经安装了pip，可以使用如下命令直接安装Flask：

```
(venv) $ pip install flask
```

再执行如下命令验证Flask是否安装成功：

```
(venv) $ python
>>> import flask
>>>
```
如上如果没有错误信息，基本安装已经完成，可以开始Flask的学习之旅了。


# 第2章 Flask应用的基本结构

本章将开始熟悉一个最基本的Flask应用的各个部分，并自己动手构建一个Flask Web应用。


## Flask应用的各个部分

### 初始化应用示例

Web服务器使用WSGI协议（Web Server Gateway Interface protocol）将所有从客户端接收到的请求传递给应用实例，这个应用实例就是一个Flask对象，通常用如下方式进行创建：

```
from flask import
Flask app = Flask(__name__)
```

关于Flask中参数的说明：Flask的构造函数只接收一个参数\_\_name\_\_，它会指向该程序片段所在的模块。目前只需要知道使用\_\_name\_\_就够了。


### 路由和视图函数

路由的作用就是将请求地址和方法关联起来，最简单的做法是通过使用应用程序实例的decorator app.route来定义一个路由:

```
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
```
当然相应内容只是一个字符串，对于想构建更复杂的response结构显然还不够，这里只是简单介绍response的概念，具体如何初始化一个更复杂的response会在第三章介绍。


很多路由上是要求能传递参数的，我们可以在路由上是配置动态参数：

```
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
```

在上例中，尖括号中间的内容是动态的，任何匹配了该形式的URL会映射到这个路由上，然后调用对应的视图方法。默认的，传递的参数被当做string处理，当然你也可以指定它们的类型，比如：


```
@app.route('/user/<int:id>')
```


### 启动Server

应用程序实例app有一个run方法用于启动Flask所集成的Web服务器：

```
if __name__ == '__main__':
    app.run(debug=True)
```

上述代码是一个常见的Python语法，if判定条件是为了保证只有该脚本被直接执行的时候才去启动server，因为如果该脚本是被当做模块引入的，那么很可能在其他的脚本中已经启动过server了。启动过后server会一直轮巡检查是否收到有客户端的请求，可以通过Ctrl+C 停止server。run方法有一些可选参数可以配置，比如设置`debug=True`能够开启调试模式。

Flask提供的Web服务器不是给产品环境用的，关于这部分内容可能要参考第十七章。


## 完整的示例代码

在前面的代码片段已经说明了该例子的各个部分，可以把flasky项目直接checkout到Tag为2a的历史节点上执行并查看效果:

*Example 2-2. hello.py: Flask application with a dynamic route*

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
```
在虚拟环境下运行hello.py，然后访问 [http://127.0.0.1:5000/](http://127.0.0.1:5000/) 即可看到Hello World页面。

```
(venv) $ python hello.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
```

![2-1.png](http://upload-images.jianshu.io/upload_images/134602-608b4912c8d5fc96.png)


你也可以尝试传递动态参数给路由，从而显示动态内容，同样你可以checkout到2b的历史节点查看效果。

```
from flask import Flask

app = Flask(__name__)

@app.route('/') def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
```

![2a.png](http://upload-images.jianshu.io/upload_images/134602-e0a28faf6c6a850b.png)


## 请求-响应的生命周期

在学会了如何构建一个基础应用程序，我们介绍一些原理性的东西帮助你理解Flask框架。

### 应用与请求的上下文

Flask接受来自客户端的请求的时候需要构建一些对象给视图方法使用，比如request对象。视图方法如何获得请求对象呢，你可以在视图方法中传递一个参数比如`def index(request)`，这样一来所有的视图方法都会增加一个参数，并且完成一个请求所需要的可能还不止一个request对象。Flask的做法是怎么样的呢？ 先来看如下这个例子：


```
from flask import request

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent
```

上述例子通过使用contexts来暂时的使得某些对象(这里是request)成为全局的，这意味着你可以直接使用一些对象就好像它们是全局对象一样。实际上上的request对象不可能是全局的，因为在一个多线程服务器中不同的线程所拥有的是来自不同的客户端的不同的请求（对象），在介绍原理之前先来参考一个表格，表格中列举了Flask中的两个contexts：application context和reqeust context，它们各自暴露了一些对变量外部使用：

![2b.png](http://upload-images.jianshu.io/upload_images/134602-080b05dec7e416e9.png)


原理是这样的：任何时候一个请求来到Flask就会激活(或者称作pushes)application context和request contexts，当请求结束再销毁它们。这意味着请求到来的时候，你可以在当前线程中获取到current_app和g，类似地reqeust和session也能被获取到。当没有激活的application context或者request context的时候，获取这些变量会报错。

如下示例证明了application context是如何工作的：

```
>>> from hello import app
>>> from flask import current_app
>>> current_app.name
Traceback (most recent call last):
...
RuntimeError: working outside of application context
>>> app_ctx = app.app_context()
>>> app_ctx.push()
>>> current_app.name
'hello'
>>> app_ctx.pop()
```
默认直接使用current_app.name是会报错的，直到我们调用了app的app_ctx的push或pop方法改变了current_app的值。`注：`这里把push和pop当做一个往current_app写入、推出application context的方法，而不要跟常见的数组的操作方法混淆了。

### 请求和试图方法的匹配

当客户端的请求来到时，我们需要找到对应的service方法（视图方法）来处理它，Flask会通过在URL map中查找当前请求URL来找到对应的service。Flask构建的map的值是由 app.route decorators和等价的nondecorator版本 app.add_url_url 初始的。

我们可以查看一下在hello.py中这个map长什么样：

```
(venv) $ python
>>> from hello import app
>>> app.url_map
Map([<Rule '/' (HEAD, OPTIONS, GET) -> index>,
     <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
     <Rule '/user/<name>' (HEAD, OPTIONS, GET) -> user>])
```
三个routes中，/ 和 /user/<name> 都是我们通过app.route decorators构建的，/static/<filename>则是Flask加的专门用来获取静态文件的，第三章会介绍更多相关知识。

HEAD, OPTIONS, GET 表示路由的视图方法所处理的请求类型，因此对于完全一样的路由，我们可以定义完全不同的视图方法。 在这里因为HEAD和OPTIONS方法都是Flask自动管理的，因此我们的三个路由都是跟GET类型绑定的 。关于请求类型在第四章会有更多的介绍。

### 钩子函数

我们通常希望请求前、后可能希望做一些通用的处理，在Flask中可以使用一些钩子函数来达到这个目的，Flask提供了四个钩子函数，含义很好理解：

- before_first_request
- before_request
- after_request
- teardown_request

钩子函数的一个典型的应用场景是：在第一次请求中通过before_first_request来获取到用户数据存储到Context中，以后请求就可以直接从Context中直接取用户数据了。

### 响应结果


#### 给返回字符串带状态码

返回给前台的数据除了可以是一个字符串，还可以携带第二个参数，下例中除了返回字符串还返回了一个400的状态码：

```
@app.route('/')
def index():
    return '<h1>Bad Request</h1>', 400
```

#### 显式使用response

你甚至还可以添加第三个参数来给response的headers添加一些设置，但是更好的做法是直接返回一个response对象。如下的例子用make_response方法构建了一个response并设置了cookie：

```
from flask import make_response
@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response
```

#### redirect

redirect是一种特殊的response，通常带有302状态码，它不包含具体的response内容而是提供一个新的URL给浏览器来加载，redirect在第四章会大量被使用。你能够通过 using a three-value return (`注`：原书内容如此不大理解含义) 或者通过response对象的方式来进行redirect，但是最通用的做法还是使用Flask提供的redirect()方法来构建redirect类型的response：

```
from flask import redirect
@app.route('/')
def index():
    return redirect('http://www.example.com')
```

#### abort

有一中特殊的response是用abort来生成的，通常被用来做错误处理。如下的例子，当根据动态参数id没有查询到相应的user的时候，会返回404的状态码。尽管abort没有返回结果，但它通过raise exception的方式跳出了处理的流程：

```
from flask import abort
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<p>Hello, %s</p>' % user.name
```

## 如何集成Flask的扩展

Flask有大量的可用于不同目的的扩展可以使用，如果这些不能满足需求，你还能找任何可用的Python包。为了演示如何在应用程序中集成扩展，如下的部分会为hello.py添加一个扩展，使应用程序能携带命令行参数。


### 带命令行选项的Flask-Script

Flask的Web Server启动时候有一些参数是可以配置的，我们可以在app.run中传入这些参数，假如我们不想改代码，只想在命令行执行的时候指定这些参数呢？该部分会介绍如何使用Flask-Script用于加强命令行的功能，使命令行能携带参数。

- 第一步，使用pip安装该扩展：

    ```
(venv) $ pip install flask-script
```
- 第二步，基于hello.py修改代码：

    ```
    from flask import Flask
    from flask.ext.script import Manager

    app = Flask(__name__)
    manager = Manager(app)

    @app.route('/')
    def index():
        return '<h1>Hello World!</h1>'

    if __name__ == '__main__':
        manager.run()
    ```
    所有的扩展都在flask.ext模块下，我们要导入的Flask-Script是从flask.ext.script模块导入，导入后名为Manager的class可以被使用。几乎所有拓展的初始化形式都是类似的：通过把Flask实例传递给模块的构造函数。当manager.run执行的时候，命令行扩展的逻辑已经被注入了。你可以checkout到2c的历史节点来查看该部分代码。


- 第三步，命令行执行：

    ```
    (venv) $ python hello.py
    usage: hello.py [-?] {shell,runserver} ...

    positional arguments:
      {shell,runserver}
        shell            Runs a Python shell inside Flask application context.
        runserver        Runs the Flask development server i.e. app.run()

    optional arguments:
          -?, --help         show this help message and exit
```

    如上，必选参数为runserver和shell, 这里我们要做的是启动Server。要查看runserver有哪些参数，可以如下方式：

    ```
    (venv) $ python hello.py runserver --help
    usage: hello.py runserver [-h] [-t HOST] [-p PORT] [--threaded]
                              [--processes PROCESSES] [--passthrough-errors] [-d]
                           [-r]
    Runs the Flask development server i.e. app.run()

        optional arguments:
        -h, --help
        -t HOST, --host HOST
        -p PORT, --port PORT
        --threaded
        --processes PROCESSES
        --passthrough-errors
        -d, --no-debug
        -r, --no-reload
```

    现在能够基于命令行直接设置server的host和port等参数了，可以将主机地址设置为0.0.0.0看看：

    ```
    (venv) $ python hello.py runserver --host 0.0.0.0
    * Running on http://0.0.0.0:5000/
    * Restarting with reloader
```

# 第3章 模板

视图方法有两个作用：处理业务逻辑（比如操作数据库）和 返回响应内容。模板起到了将两者分开管理的作用，本章介绍模板引擎Jinjia2。

## Jinjia2模板引擎


模板只是一些包含文本的字符串，设置的变量标记位最终会被模板引擎用数据渲染。要使用Jinjia2模板，第一步是定义模板，Jinjia2默然会到项目的子目录templates中寻找模板，所以在该目录下定义两个模板文件：

*Example 3-1. templates/index.html: Jinja2 template*:

    <h1>Hello World!</h1>

 *Example 3-2. templates/user.html: Jinja2 template*：

    <h1>Hello {{name}}!</h1>

### 渲染模板

稍加修改*hello.py*, 导入模板渲染方法render_template，然后调用该方法注入模板。render_template方法的第一个参数是模板文件名称，后面的参数是在模板中会被引用到的变量：

*Example 3-3. hello.py: Rendering a template*


    from flask import Flask, render_template

    #...

    @app.route('/index')
    def index():
    return render_template('index.html')

    @app.route('/user/<name>')
    def user(name):
        return render_template('user.html', name=name)

启动server以后可以分别访问相对路径`/index`和`/user/<name>`索引来查看页面内容结果。你也可以checkout到3a的历史节点来运行代码并查看效果。

### 变量类型

模板中不仅能使用字符串数字等简单的数据类型，还能接收复杂的数据结构，比如dict、list、obj，然后你可以在模板中通过如下的形式来使用这些变量：

*templates/vars.html*:

    <p>A value from a dictionary: {{ mydict['key'] }}.</p>
    <p>A value from a list: {{ mylist[3] }}.</p>
    <p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
    <p>A value from an object's method: {{ myobj.somemethod() }}.</p>


*hello.py*

    class Human():
        def somemethod(self):
            return 'what the fucking world!'

    @app.route('/vars')
    def user(name):
        mydict = {"key": "To Be or Not To Be"}
        mylist = ['it', 'is', 'a', 'problem']
        myintvar = 0
        myobj = Human()

        return render_template('vars.html', mydict=mydict, mylist=mylist, myintvar=myintvar, myobj=myobj)

除了使用复杂的数据结构以外，模板中还能对值进行过滤，下面是一个简单的将内容变为大写的例子。

```
Hello, {{ name|capitalize }}
```

![3-1.png](http://upload-images.jianshu.io/upload_images/134602-04c5abf058b1f8aa.png)


尤其说明下safe这个filter，当变量内容为`'<h1>Hello</h1>'`时，默认地Jinjia2会将内容渲染为 `'<h1>Hello</h1>'`，而很多场景中可能会需要在变量中存储模板内容，因此在确保内容安全的前提下你可以使用safe这个filter从而不去转移变量值。关于filter的完整列表可以参考官方的文档：[Official Jinja2 Documentation](Official Jinja2 Documentation)。

### 控制结构

Jinjia2能够使用常见的控制流，如下是常用的几种控制流：

#### if else


*hello.py*

```
@app.route('/flow')
def flow():
    user = 'tangyefei'
    return render_template('flow.html', user=user)
```

*templates/flow.html*

```
{% if user %}
    Hello, {{user}}
{% else %}
    Hello, stranger
{% endif %}
```

#### for

*hello.py*

```
@app.route('/loop')
def loop():
    comments = ["To Be", "Or", "Not To Be"]

    return render_template('loop.html', comments=comments)
```

*templates/loop.html*

```
<ul>
   {% for comment in comments%}
        <li>{{comment}}</li>
    {% endfor %}
</ul>
```

#### macro

我们可以把部分模板渲染内容抽到macro，其他的地方可以调用macro方法进行渲染

*hello.py*

```
@app.route('/macro')
def macro():
    comments = ["To Be", "Or", "Not To Be"]
    return render_template('macro.html', comments=comments)
```

*templates/macro.html*

```
{% macro render_comment(comment) %}
    <li>{{comment}}</li>
{% endmacro %}
<ul>
     {% for comment in comments%}
        {{ macro.render_comment(comment) }}
    {% endfor %}
</ul>
```

#### 外部导入Macro

*hello.py*

```
@app.route('/comments')
def comments():
    comments = ["To Be", "Or", "Not To Be"]
    return render_template('comments.html', comments=comments)
```

*templates/macro.html*

```
{% macro render_comment(comment) %}
    <li>{{comment}}</li>
{% endmacro %}
```

*templates/comments.html*

```
{% import 'macro.html' as macros %}
<ul>
     {% for comment in comments%}
        {{ macros.render_comment(comment) }}
    {% endfor %}
</ul>
```

#### 模板继承

*hello.py*

```
@app.route('/extends')
def extends():
    return render_template('child.html')
```

*/templates/base.html*

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% block head%}
        <title>
            {% block title%}{% endblock%}- My Application
        </title>
    {% endblock %}
</head>
<body>
    {% block body%}
    {% endblock%}
</body>
</html>
```

*/templates/child.html*

```
{% extends 'base.html'%}
{% block title%}
    Index
{% endblock %}
{% block head%}
    {{ super() }}
    <style>
    </style>
{% endblock%}
{% block body%}
    <h1>Helll, World!</h1>
{% endblock%}
```

## Jinjia2集成Bootstrap

要使用Bootstrap，要在每个模板中引入它的JavaScript和CSS，我们可以通过使用Flask-Bootstrap来简化这个过程。安装Flask-Bootstrap后，我们只需要在自己模板中继承bootstrap/base.html，它包含了BootStrap的JavaScript和CSS的模板并且定义了很多类型的block，我们可以在子类中复写它们。这里是一个使用Flask-Bootstrap的例子：


### 第一步，安装flask-bootstrap

```
(venv) $ pip install flask-bootstrap
```

### 第二步，导入flask-bootstrap

*Example 3-4. hello.py: Flask-Bootstrap initialization*

```
from flask.ext.bootstrap import Bootstrap
bootstrap = Bootstrap(app)

@app.route('/bootstrap/<name>')
def bootstrap(name):
    return render_template('bootstrap.html', name=name)
```

### 第三步，构建模板覆写父模板

```
{% extends 'bootstrap/base.html'%}

{% block title%} Flasky {% endblock %}
{% block navbar%}

    <div class="navbar navbar-inverse" role="navigation">
        <div class="container">
            <div class="navbar-header">
            <button type="button" class="navbar-toggle"
            data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">Flasky</a> </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li><a href="/">Home</a></li>
                </ul>
            </div>
        </div>
    </div>
{% endblock %}
{% block content%}
    <div class="container">
        <div class="page-header">
        <h1>Hello, {{ name }}!</h1> </div>
    </div>
{% endblock %}
```

如下是上述例子效果图，你也可以把代码checkout到3b的历史节点来查看效果：

![3-2.png](http://upload-images.jianshu.io/upload_images/134602-171de35a2f3e67a5.png)


除了上面用到的block以外，Flask-Bootstrap还定义了一些其他的block能够被子模板覆写。

![3a.png](http://upload-images.jianshu.io/upload_images/134602-78daba8f58915cd3.png)


上表的很多block在Flask-Bootstrap的base.html就被使用到了（比如styles和scripts这两个blocks），因此你如果还需要加入自己的内容，可以使用super()方法来获取到父模板的内容然后在后面追加自己的内容：

```
{% block scripts %}
    {{ super() }}
    <script type="text/javascript" src="my-script.js"></script>
{% endblock %}
```

## 定制错误页面

我们需要为一些错误状态比如404、500来定制错误页面，为了保证错误页面和我们之前写的user.html页面一样有一致的头部，我们可以把user.html的一些共有部分拷贝用来，然后基于此构造出我们的404.html和500.html。在此之前先让我们定义404和500的视图方法：

*Example 3-6. hello.py: Custom error pages*

```
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
```

模板的继承让404.html和500.html的构建变得更简单了，既然所有页面会有一些共有的头部，那么我们把这些共有部分放在templates/base.html，并且继承自bootstrap/base.html。

*Example 3-7. templates/base.html: Base application template with navigation bar*

```
{% extends "bootstrap/base.html" %}
{% block title %}Flasky{% endblock %}
{% block navbar %}
<div class="navbar navbar-inverse" role="navigation">
    <div class="container">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">Flasky</a>
        </div>
        <div class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li><a href="/">Home</a></li>
            </ul>
        </div>
    </div>
</div>
{% endblock %}
{% block content %}
    <div class="container">
        {% block page_content %}{% endblock %}
    </div>
{% endblock %}
```

  可以看到我们新增了一个名为page_content的block，意味着子模板只需要在这个block中复写内容。

*Example 3-8. templates/404.html: Custom code 404 error page using template inheri‐ tance*

    {% extends 'templates/base.html'%}

    {% block title%} Page Not Found{% endblock%}
    {% block content %}
        <div class="page-header">
            <h1>Not Found</h1>
        </div>
    {% endblock%}

你可以通过把代码checkout到3c的历史节点来执行并查看效果。下图显示了当访问一个不存在的地址时，页面的显示内容：

![Example 7-1.png](http://upload-images.jianshu.io/upload_images/134602-747ecf0611640de1.png)


## 用url_for来获得路由地址

任何一个包含多个链接的站点都免不了要进行链接的相互跳转，其中有一些地址还是动态的，除了常规的在页面format好链接地址外，你还可以通过url_for方法来指定要跳转到的地址，它的第一个参数是视图方法的名称，这意味这哪怕路由地址某些部分被重命名了你的代码依旧有效。

比如 url_for('index')会请求到 /, 而 url_for('index', _external=True)会请求到绝对地址 http://localhost:5000/ ，因为相对地址比绝对地址更有效率，因此应该尽可能使用相对地址。

通过传递给url_for()键值对，我们可以构建动态地址，比如  url_for('user', name='john', _external=True)会请求到 http://localhost:5000/user/john。

如果你传递了一些动态路由上不要的参数，它会被当做查询参数跟在链接地址后面，比如url_for('index', page=2)会返回 /?page=2。

## 静态文件

一个Web应用除了Python代码和模板文件以外，还会有一些静态资源文件，比如图片、JavaScript和CSS文件。在第二章中我们看到了url_map中有一个路由是 /static，相当于任何静态文件的请求都会被/static/<filename>这个路由处理。比如调用 url_for('static', filename='css/styles.css', _external=True)  最终会返回http://localhost:5000/static/css/styles.css。 如下示例尝试在base.html模板文件中包含favicon.ico作为tab的icon，你可以checkout代码到3d的历史节点并执行查看效果：

*Example 3-10. templates/base.html: favicon definition*

    {% block head %}
        {{ super() }}
        <link rel="shortcut icon" href="{{ url_for('static', filename = 'favicon.ico') }}" type="image/x-icon">
        <link rel="icon" href="{{ url_for('static', filename = 'favicon.ico') }}" type="image/x-icon">
    {% endblock %}

## 使用Flask-Moment来格式化时间和日期

服务器端的时间格式跟客户端显示无关，通常统一用UTC来表示，对于客户端用户则需要用本地化的日期和时间格式。因为浏览器能够获取到所在时区等信息，因此在浏览器端来构建时间日期的格式是比较合理的。moment.js是一个优秀的客户端JavaScript库，在Flask-Moment中我们把moment.js与Jinjia2模板进行了集成。 你可以使用pip安装Flask-Moment：

```
(venv)$ pip install flask-moment
```

如下例在程序中导入Flask-Moment:

*Example 3-11. hello.py: Initialize Flask-Moment*

```
from flask.ext.moment import Moment
moment = Moment(app)
```

Flask-Moment需要依赖jquery.js和moment.js，必须要在HTML页面中导入这两个库。因为Bootstrap中已经包含了jquery.js, 我们只需要导入moment.js即可。如下例子展示了如何在base.html中导入moment.js：

Example 3-12. templates/base.html: Import moment.js library

```
{% block scripts %}
{{ super() }}
{{ moment.include_moment() }}
{% endblock %}
```

导入成功以后我们就可以在模板中使用moment的功能了：

*Example 3-13. hello.py: Add a datetime variable*

```
from datetime import datetime
@app.route('/') def index():
    return render_template('index.html', current_time=datetime.utcnow())
```

*Example 3-14. templates/index.html: Timestamp rendering with Flask-Moment*

```
<p>The local date and time is {{ moment(current_time).format('LLL') }}.</p>
<p>That was {{ moment(current_time).fromNow(refresh=True) }}</p>
```
你可以checkout到3e历史节点执行和查看效果。format('LLL')会按照本地的时区和设置来format时间，参数决定了format的格式，从'L'到'LLL'决定了不同准度的格式，除此外还可以接受自定义的格式。fromNow()方法显示了相对的时间值，refresh=True的设置会使页面随着时间推移而自动刷新时间。

Flask-Moments实现了来自moment.js的 format(), fromNow(), fromTime(), calendar(), valueOf(), 和 unix() 方法，可以通过[documentation](http://momentjs.com/docs/#/displaying/)来参考不同的format选项。`注`：Flask-Moment假定服务端处理的时间是用UTC格式表示的原生date-time对象。可以参考[datetime](https://docs.python.org/2/library/datetime.html)包的具体信息。

Flask-Moment构建的时间格式能够本地化成不同的语言格式，只需要在模板中传入语言编码给lang()方法（`注`：下述设置个人实测不管用，无论是设置成'fr'或者其他语言都一样）：

```
    {{ moment.lang('es') }}
```


通过使用本章介绍的只是基本能够构建出友好的客户端代码了，下一章要介绍和用户交互的表单。
为了解决表单验证之类的重复和繁琐的问题，可以引入Flask-WTF来让表单使用变得简单（注：如果不使用Flask自带的模板，而是用Angular.js等前端技术本章可以略过，因为表单验证是跟Jinjia2模板紧密关联在一起的）。通过pip安装：

    (venv) $ pip install flask-wtf

# 第4章 表单

在第2章中我们介绍了request对象，所有来自客户端的信息都被存储在了这个对象中，特别地你可以通过 request.form来获得POST请求所提交的表单数据。在处理表单的时候，有一些工作是繁琐并且有重复性的，两个比较好的例子是：表单代码的构建、表单数据的验证。 Flask-WTF是一个基于WTForms（和表单相关的并且独立于框架的Python包）的Wrapper，它能让我们处理这些任务更加容易。你可以使用pip来安装它：

```
(venv) $ pip install flask-wtf
```

通过执行如上安装，Flask-WTF以及它的依赖库就都装好了。

## 跨站点伪装请求(CSRF) 保护

当一个用户登录了一个恶意站点，这些站点会向一些该用户登录过的其他站点发送请求，CSRF通常就发生在这个时候。默认地Flask-WTF会保护表单免受CSRF的攻击，但你得要设置一个加密的Key，Flask-WTF会使用这个Key来初始化化一个token，这个token会被用来验证来自表单的数据是否被授权。

如下例子展示了如何配置一个加密的Key：

*Example 4-1. hello.py: Flask-WTF configuration*
    app = Flask(name)
    app.config['SECRET_KEY'] = 'hard to guess string'
￼
app.config对象常被来存储一些配置信息，只需要使用常规的字典的存取方法即可。你也可以从文件或者其他环境中导入配置。SECRET_KEY变量经常被Flask和第三方的扩展当做常规加密的Key，因为密码的强壮程度跟这个变量有关，要尽可能设置成没人知道的值并且在不同的应用中不要设置相同的值。


`注`：为了加强安全性，secret key应该被存储在环境变量中，第7章会介绍相关的知识。

## 表单类和表单属性

当使用Flask-WTF的时候，每个Web表单都属于继承自Form的类，类里面定义了一些列的属性，每个属性又有一个或者多个的校验器。

*Example 4-2. hello.py: Form class definition*

```
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
```

表单的每个属性都属于类的属性，他们都是跟属性类型相关联的对象，在上述这个例子中，NameForm有一个叫做name的文本框，和一个叫submit的提交按钮。StringField类用于表示一个type="text"的`<input>`节点，SubmitField类用于表示一个type="submit"的`<input>`节点，它们的构造函数的第一个值是在HTML渲染中会被用作label的文本内容。StringField中包含的可选的校验器 Required()用于确保被提交数据不为空。

注：Form是从Flask-WTF中定义的因此从flask.ext.wtf.中导入的，但是属性类和验证类是从WTForms中直接导入的。

*Table 4-1. WTForms standard HTML fields*


![Figure 4-1.png](http://upload-images.jianshu.io/upload_images/134602-27c53e00f7448e65.png)


*Table 4-2. WTForms validators*

![Figure 4-2.png](http://upload-images.jianshu.io/upload_images/134602-eec490113e132d7d.png)



## 在HTML中渲染表单对象

表单类的属性都是可以调用的，在模板中调用它们后他们会被渲染到HTML中。假定有一个表单类NameForm的对象实例是form，我们能够用如下方式来构建HTML：

```
<form method="POST">
    {{ form.name.label }} {{ form.name() }}
    {{ form.submit() }}
</form>
```

显然这样还太单调了，你还可以通过设置id或者class方便给这些组件添加样式:

```
<form method="POST">
    {{ form.name.label }} {{ form.name(id='my-text-field') }}
    {{ form.submit() }}
</form>
```

我们需要花费很多的时间来美化表单，我们最好吧Bootstrap导入并应用到表单中，使用Flask- Bootstrap以后，之前的表单要改成这个样子：

```
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
```

上例中bootstrap/wtf.html定义了工具方法可以使用Boostrap的预定义样式来渲染Flask-WTF表单，wtf.quick_form()把表单的对象实例作为参数。如下为完整实例代码：

*Example 4-3. templates/index.html: Using Flask-WTF and Flask-Bootstrap to render a form*

```
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}

{% block title %}Flasky{% endblock %}

{% block page_content %}
    <div class="page-header">
        <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
    </div>
    {{ wtf.quick_form(form) }}
{% endblock %}
```
内容区域分为两个部分，第一部分是显示问候语的header部分，这里有name的条件判定，会根据name是否存在而显示不同的问候语；第二部分则使用wtf.quick_form()方法来渲染form实例。


## 表单响应

如下为修改后的index()方法，在这个视图方法中，不仅包含定义表单对象还要能接收来自表单的数据：

*Example 4-4. hello.py: Route methods*

```
@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)
```


添加到app.route这个decorator的方法包含了GET和POST，当请求参数没有指定方法类型时候会被当做GET请求。而给表单提交增加POST方法是一种常规的做法，因为POST方法有请求体，而GET方法只能把参数追加到在地址栏上。 上例中视图方法构建了一个NameForm类的示例，用于显示前面展示的表单，validate_on_submit()方法只当有表单提交并且所有校验通过时候返回True，返回值决定了视图方法的流程。

当用户第一次访问到这个页面的时候，服务器接收到一个GET方法请求，validate_on_submit() 返回False，if分支内的内容会跳过；当用户通过POST方法来提交请求时，validate_on_submit()调用Required()来验证name属性，如验证通过，if内的逻辑会被执行。而模板内容最后会被渲染到页面上。你可以checkout到4a的历史执行并查看效果：



*Figure 4-1. Flask-WTF web form*

![Figure 4-3.png](http://upload-images.jianshu.io/upload_images/134602-576c2205949174ae.png)


*Figure 4-2. Web form after submission*

![Figure 4-4.png](http://upload-images.jianshu.io/upload_images/134602-7197c236a5fc2943.png)


当name输入为空时，点击Submit提交会失败，并且有提示信息给用户：

*Figure 4-3. Web form after failed validator*
![Figure 5-1.png](http://upload-images.jianshu.io/upload_images/134602-a0b0287ce107a027.png)


## 重定向和用户Session


前一小节中的hello.py使用时会遇到一个问题，当你输入name点击提交，然后再刷新浏览器你会收到表单重复提交的确认提示。因为浏览器刷新的时候会重复一次最后发的请求，如果这个请求是POST类型，就会导致重复提交表单，当然多数时候这不是我们想要的结果。因为多数用户跟本不知道这个确认提示表示什么含义，所以最好的做法是永远不要把POST请求当做浏览器发送的最后一个请求。

为了达成这个目的，我们可以使用redirect来替代直接的POST请求，一个redirect只是一种特殊类型的response，它包含要定位到的URL，这个URL决定了最终显示的内容。当浏览器收到redirect类型的response，它会从这个URL上去用GET方式请求内容。尽管这个过程会稍微多花一点点时间 ，但是用户根本觉察不到这个过程。这么做了以后，我们的最后一个请求就是GET类型了，刷新页面也不会导致表单重复提交的问题。这个策略叫做： Post/Redirect/Get Pattern。

这种策略随之而来的一个问题是，当接收POST请求的时候，我么可以从form.data.name中获取数据，请求结束后数据就丢失了。因为我们返回了redirect类型的response需要考虑到redirect后的请求如何获取POST所提交的数据，因此应用程序需要读取name并且存储起来给redirect后的请求用。

应用程序能够通过user session来存储数据，正如在第2章介绍的，user session是跟request context相关联的，session的使用就像标准的字典类型那样。如下是经过修改后实现了redirect和user session的index()版本：

*Example 4-5. hello.py: Redirects and user sessions*

```
from flask import Flask, render_template, session, redirect, url_for
@app.route('/', methods=['GET', 'POST']) def index():
form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))
```


之前我们使用name变量来存储用户在表单中输入的名字，现在改为session['name'], 来自表单提交的请求会直接返回一个redirect类型的response。redirect()以一个URL为参数，我们需要传入一个相对于根的URL，在这里是redrirect('/')，但是我们可以使用之前介绍过的url_for()，只需要传入视图方法即可得到URL。另外一项改动是render_template中的name的值，因为我们已经把数值存储到了session中，所以现在要从session中去取name的值。

你可以把代码checkout到4b上来执行查看效果，再次提交刷新后你会发现浏览器没有再弹出重新提交的提示了。

## 消息提示

当一个请求结束后给用户一些状态提示是很有用的，比如一些确认信息、警告或者错误提示。一个典型的例子就是当用户提交错误的登陆信息，服务器应该响应一个错误提示告诉用户。Flask的核心里面包含了这么一个功能，如下例子展示如何使用 flash()来达到这个目的：

*Example 4-6. hello.py: Flashed messages*

```
from flask import Flask, render_template, session, redirect, url_for, flash

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',form = form, name = session.get('name'))
```

在这个例子中，每次提交的name都会用来跟已经存储的name进行比较，如果两次的值不同，flash()会被调用并传递一个消息给前台用于展示。为了保证所有的页面都能够展示提示信息，我们最好把展示信息的相关内容写在base.html中。get_flashed_messages()方法能拿到所有通过flash()推送的消息，下面是在前台模板中如何接收和使用这些消息的示例：


*Example 4-7. templates/base.html: Flash message rendering*

```
{% block content %}
    <div class="container">
        {% for message in get_flashed_messages() %}
        <div class="alert alert-warning">
            <button type="button" class="close" data-dismiss="alert">×</button>
            {{ message }}
        </div>
        {% endfor %}
            {% block page_content %}{% endblock %}
    </div>
{% endblock %}
```

因为get_flashed_messages()获取的可能是多次flash()的消息列表，所以模板中使用了循环来展示这些消息。当页面刷新的时候，相当于重新请求get_flashed_messages()，之前展示过的消息自然也没有了。

![Figure 5-2.png](http://upload-images.jianshu.io/upload_images/134602-3a4a9ecc013fcc60.png)



你可以checkout到4c的代码节点执行和查看效果。一个应用的基础功能是要能够接收来自表单提交的数据并持久化地存储这些数据，这正是下一章的数据库要介绍的内容。

# 第5章 数据库

## 数据库简介

数据库以一定的组织结构来存储数据，应用程序能按照需求读取不同的数据值。Web应用程序所最普遍使用的是基于关系模型的数据库，也称作SQL数据库，名称来源于它使用的查询语言Structured Query Language。但是近些年基于文档的、键值型的NoSQL数据库开始变得流行。

### SQL数据库


关系型数据库中，所有的数据都存储在表中，这些表用来给应用程序的实体建模。比如，一个订单管理系统中可能会包含customers, products和orders表。 一个表有固定数目的列和可变数目的行，列定义了表格对应的建模实体的属性。比如一个customers表会有name, address, phone等列。行定义了一个真实的数据条目，其中包含了所有列中的属性的值。

每个表中有一个特殊的列叫做primary key，它是每一行的唯一标识，表格还可能会有叫做foreign key的列，它会引用来自另一个表的某一行的primary key值，两个不同的表的两行通过这种方式建立起联系是关系型数据库的基础。下图展示了一个包含了users和user roles的数据库的图表，两者之间的线表现了表之间的关系。

![Figure 8-1.png](http://upload-images.jianshu.io/upload_images/134602-ea422b497d484bee.png)

*Figure 5-1. Relational database example*

在这个图表中，roles表存储了所有角色，每个用id值（primary key）来进行唯一标识。users表包含了一系列的users，每个同样拥有唯一的id值。除了id这个primary key，roles 表还有一个name列，users表还有usersname和password列。其中users表中的role_id列是一个foreign key用于引用role的id，通过这种方式我们就能知道一个用户的角色。

通过如上例子我们知道，关系型数据库有效率地存储了数据，避免了重复。对一个角色进行重命名意味着只需要改一个地方即可，一旦role的名字改变，通过role_id来关联的users的角色名字也会相应改变。另一方面，将数据拆分到不同的表格中会导致一个小问题，因为users和roles需要从不同的表中读取并关联起来。但关系型数据库为多表间的关联查询提供了支持。

### NoSQL数据库

只要不是按照前一节的方式来组织数据的数据库都被统称为NoSQL数据库，一个常用的结构是使用集合而非表或者文档来存储数据记录。NoSQL数据库被设计成不支持关联操作，因此多数NoSQL类型的数据库完全不支持这样的操作。对于前一小节中的数据库结构，用NoSQL的方式来存储的话，如果要读取所有包含角色名的用户需要应用程序自己去做关联操作，即先读取所有的users信息，然后根据每个user的role_id来查询对应的role。

一个更加符合NoSQL数据库结构的图表如下，这是使用了denormalization操作的结果，通过使用denormalization减少了表格的数量，但是增加了重复数据带来的开销。

![Figure 8-2.png](http://upload-images.jianshu.io/upload_images/134602-b9dc94162c147680.png)

*Figure 5-2. NoSQL database example*


### 选择SQL还是NoSQL数据库

SQL数据库在处理结构化的数据非常有优势，这些数据库通常保持结构一致性，而NoSQL数据库则解放了结构一致的限制。本书不做详细的比对，但是对于小型和中型的应用，SQL和NoSQL数据库都能完全符合要求并且不会在性能上有太大差异。


## Python数据库工具选择

你能找到大多数的数据库引擎的Python包，它们不仅开源还有社区支持。Flask并不限定数据库包的选择，你能够使用MySQL, Postgres, SQLite, Redis, MongoDB 或 CouchDB中的任何一种。

如果这些选择还不够，你还可以选择包的抽象层，比如：SQLAlchemy、MongoEngine。它们允许你在更高的层次上直接和Python对象打交道而不是和数据库实体对象（tables、documents、query languages）打交道。

通常在选择数据库工具的时候都会有如下几个参考标准：

### 易用性

数据库抽象层，又被称作object-relational mappers (ORMs) 或 object-document mappers (ODMs)，提供了从高级对象到低级数据库实体的直接转换，使用起来当然会更加方便。

### 性能

ORMs和ODMs把对象转化为数据库实体会有一些开销，但多数时候这个开销可以忽略不计的。通常来说，使用ORMs和ODMs带来的工作效能提升往往大于所带来的性能损耗，因此我们没有什么理由拒绝ORMs和ODMs。通常比较合理的做法是用数据库抽象层来做常用的操作，而只在某些需要特别优化的地方使用原生的数据库操作。

### 可移植性
所选择的数据库在生产和部署环境下是否可用是一个必须考虑的因素，比如你想要把你的应用部署在云平台上，你当然应该首先知道该平台支持哪些数据库。

ORMs和ODMs还能带来的其他一个便利。虽然多数数据库提供了一个抽象层，但是还有一些更高阶的抽象层提供了只用一套接口即可操作多种数据库的功能。最好的例子就是SQLAlchemy ORM，它提供了一系列关系型数据库引擎的支持，比如MySQL、Postgres 和 SQLite。

### 和Flask集成

尽管不是必须要求能和Flask集成，但是能和Flask集成意味着能为你省去你大量书写代码的时间 。正是因为使用Flask集成的数据库引擎能简化配置和操作，你应该尽可能选择Flask扩展形式的数据库引擎包。综上，本书将会选择Flask-SQLAlchemy作为数据库工具，它是一个基于SQLAlchemy的Flask扩展。

## 使用Flask-SQLAlchemy进行数据库管理


SQLAlchemy 是一个强大的关系型数据库框架，它提供了高层的ORM 和 底层的原生数据库的操作，并且它能够支持多种数据库。Flask-SQLAlchemy是一个简化了SQLAlchemy操作的Flask扩展。 可以通过pip进行安装Flask-SQLAlchemy：

```
(venv) $ pip install flask-sqlalchemy
```

在Flask-SQLAlchemy中数据库都会被定义为URL形式，如下表格展示了三个主流数据库的URLs:

*Table 5-1. Flask-SQLAlchemy database URLs*

![Figure 8-3.png](http://upload-images.jianshu.io/upload_images/134602-b13a26afeb8996ea.png)



其中hostname为服务器地址，可能是localhost或者一台远程服务器，数据库服务器上可能有多个数据库因此database用来指定数据库的名称，对于需要进行身份验证的数据库还需要提供username和password。SQLite数据库没有服务器，只是一个文件系统，因此hostname和username、password都可以省略。


数据库URL被在配置在Flask的config对象的 SQLALCHEMY_DATABASE_URI 中，还有另一个重要的属性被配置在 SQLALCHEMY_COMMIT_ON_TEARDOWN 中用来在每次请求结束时候自动提交数据库改动，Flask-SQLAlchemy官方文档提供了更多配置选项。如下是一个配置SQLite数据库的例子：

*Example 5-1. hello.py: Database configuration*


```
from flask.ext.sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
```
db是一个实例化了了的SQLAlchemy对象，它提供了所有Flask-SQLAlchemy中提供的功能。


### Model定义

model是指那些在应用中被持久化的对象，在ORM的环境下，一个model是一个典型的Python类的对象，它包含了一些跟数据库表的列对应的属性。Flask-SQLAlchemy数据库的实例提供了一个model的基类和一系列的工具方法方法来定义他们的结构，在前面示例中的roles和users表格可以定义成如下的Role和User models:

*Example 5-2. hello.py: Role and User model definition*

```
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username
```

类变量 \_\_tablename\_\_ 定义了表名，尽管\_\_tablename\_\_没有设置时Flask-SQLAlchemy会给它一个默认名字，但是复数形式转换的的不太好，所以最好还是单独命名。其他的则是model的属性，定义为db.Column类的实例。db.Column构造函数的第一个参数是模型属性跟数据库列对应的类型，如下表格展示了可用的数据库列的类型以及对应的在Python中的类型：

*Table 5-2. Most common SQLAlchemy column types*

![Figure 8-4.png](http://upload-images.jianshu.io/upload_images/134602-7b596f6441d5ad64.png)

![not-found.png](http://upload-images.jianshu.io/upload_images/134602-f745aa67eb255b0e.png)


Flask-SQLAlchemy要求所有的model都定义一个primary key列，通常这个列被命名为id。虽然不是严格要求model都实现\_\_repr\_\_方法，但在上述中的两个model中都添加这个方法可以方便在调试和测试时阅读。

### 关系

关系型数据库通过relationships的使用来在不同的表的行之间建立联系，在Figure 5-1中我们展现了users和roles之间的关系。它们是属于one-to-many的关系，因为一个角色属于多个用户，而多个用户都是只能有一个角色。如下示例表示了如何在model类中表示这种关系：

*Example 5-3. hello.py: Relationships*

```
class Role(db.Model):
    # ...
    users = db.relationship('User', backref='role')
class User(db.Model):
    # ...
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
```

在Figure 5-1中relationship通过foreign key来建立两表中行与行之间的关系，User model中的role_id被定义为foreign key，db.ForeignKey()中的"roles.id"指定了role_id的值会去roles表和id属性关联。

Role model中定义了users属性，任何一个Role的实例，users都会返回一个和该role关联的users列表。db.relationship()的第一个参数制定了users要关联的model名称，backred参数则通过在User model中添加一个role属性实现了反转控制。

多数时候db.relationship()能够定位到关系的foreign key指向哪里，但是有时候不行。比如一个Use model有两个或者多个列被定义为Role的外键，那么SQLAlchemy不知道该使用哪一个。不论foreign key配置是否明确要求，db.relationship()的第二个参数都应该加上。Table 5-4列举了能被用来定义relationship的常用的配置选项：

*Table 5-3. Common SQLAlchemy relationship options*
![Table 4-1.png](http://upload-images.jianshu.io/upload_images/134602-67e75f9a01e94ce9.png)


你可以把代码checkout到5a的节点来查看。

除了one-to-many的关系以外，one-to-one的关系也能通过使用one-to-many的方式来表示，只需要在db.relationship()中设置uselist为False，这样就吧对“多”变成了对“一”。many-to-one 的关系也能用one-to-many来表达，只需要表格倒过来即可，or it can be expressed with the foreign key and the db.relationship() definition both on the “many” side（`注`：原文此处不大理解）。复杂的many-to-many关系则需要建立中间表，在第十二章会专门介绍它.

### 数据库操作


既然models已经按照Figure 5-1所设计的那样被定义出来了，下一步就是学习如何使用这些models了，学习如何使用models跟数据库打交道的最好办法是在Python Shell中，如下部分将开始学习最常见的数据库操作：

#### 创建表格

最首先要做的事情是使用db.create_all()来创建数据库表，它基于models类实例来进行表的构建：

```
(venv) $ python hello.py shell
>>> from hello import db
>>> db.create_all()
```

如果你有检查过应用所在目录会发现多了一个data.sqlite的文件，这是我们在配置中指定的sqlite的数据库的名字，如果表已经存在了的话db.create_all()方法不会重新创建或者更新数据库表结构。这样对于想更改表结构可能不太方便，你可以采用删除表格让后重新创建的方式。

```
>>> db.drop_all()
>>> db.create_all()
```

当然这样做意味着所存储数据也丢失了，更好的做法会在本章的末尾进行介绍。

#### 插入数据行

如下例子尝试插入users和roles的一些数据行：

```
>>> from hello import Role, User
>>> admin_role = Role(name='Admin')
>>> mod_role = Role(name='Moderator')
>>> user_role = Role(name='User')
>>> user_john = User(username='john', role=admin_role)
>>> user_susan = User(username='susan', role=user_role)
>>> user_david = User(username='david', role=user_role)
```

models的构造函数接收属性值作为参数，注意虽然role属性被使用了，但它不是真正的数据库列，它只是一个高层次的one-to-many的relationship的展示。这些role的id都还没有被设置：因为它们是由Flask-SQLAlchemy来维护的，到目前为止它们只是一些Python对象：

```
>>> print(admin_role.id)
None
>>> print(mod_role.id)
None
>>> print(user_role.id)
None
```

所有数据库改动都被记录到了数据库提供的session中，这里你可以通过Flask-SQLAlchemy的db.session获取到它，为了把对象写到数据库它们必须先保存到session中：

```
>>> db.session.add(admin_role)
>>> db.session.add(mod_role)
>>> db.session.add(user_role)
>>> db.session.add(user_john)
>>> db.session.add(user_susan)
>>> db.session.add(user_david)
```

或者更简单地：

```
>>> db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])
```

然后你要把所有的数据库改动提交：

```
>>> db.session.commit()
```

这时可以检查id属性值：

```
>>> print(admin_role.id)
1
>>> print(mod_role.id)
2
>>> print(user_role.id)
3
```

`注`：数据库的session跟第四章讨论的Flask的session没有关联，数据库的session又被称作transactions。

数据库session对于保证数据的一致性非常重要，commit操作会把所有保存到session中的对象一次提交（原子性），如果发生了错误所有session中的对象提交都会被取消。如果你总是把相关改动放在一个session中一次性提交，这样就能避免因为只有部分改动提交成功导致的数据库不一致性。

数据库也能回滚操作，如果db.session.rollback()被调用，所有数据库session中的对象都会恢复到数据库中的状态。`注`：不是很理解，不是重置数据库中的值吗，怎么成了使session中的值跟数据库一致了？


#### 修改数据行

数据库session中的add()方法同样也能被用于更新models，如下的例子把role从“Admin”重命名为“Administrator”：

```
>>> admin_role.name = 'Administrator'
>>> db.session.add(admin_role)
>>> db.session.commit()
```

#### 删除数据行

可以使用session中的add()方法来删除数据，更其他操作一样，删除也要通过session.commit()才能生效：

```
>>> db.session.delete(mod_role)
>>> db.session.commit()
```

#### 查询数据行

Flask-SQLAlchemy使model类查询对象成为可能，最基本的model的查询操作是返回整个表格的数据：

```
>>> Role.query.all()
[<Role u'Administrator'>, <Role u'User'>]
>>> User.query.all()
[<User u'john'>, <User u'susan'>, <User u'david'>]
```

你还可以通过配置过滤器来限制查询条件：

```
 >>> User.query.filter_by(role=user_role).all()
[<User u'susan'>, <User u'david'>]
```

还可以获取到SQLAlchemy生成的原生的查询语句：

```
>>> str(User.query.filter_by(role=user_role))
'SELECT users.id AS users_id, users.username AS users_username,
users.role_id AS users_role_id FROM users WHERE :param_1 = users.role_id'
```

如果关闭了shell窗口以后，之前创建的Python对象就都消失了，但是会存在于数据库表中。你可以开一个新的窗口，然后导入model并重建这些对象。如下一个未曾导入就尝试查询名字为“User”的role的例子：


```
>>> user_role = Role.query.filter_by(name='User').first()
```

正确的做法是：

```
>>> from hello import Role
>>> user_role = Role.query.filter_by(name='User').first()
```

query对象调用形如filter_by()的方法后会返回一个新的query，你可以按照序列方式构建多个filters。Table 5-5展示了常用来查询的一些fitlers，完整的列表可以参考[SQLAlchemy documentation](http://docs.sqlalchemy.org/en/rel_1_0/)。

*Table 5-5. Common SQLAlchemy query filters*

![Table 4-2.png](http://upload-images.jianshu.io/upload_images/134602-bc3e30d970c512fe.png)


在所有的filters都被应用到了query以后，你可以调用all()来执行得到所有的查询结果，但是你可以通过其他方法来获取查询结果，Table 5-6列举了可用的execution方法：

*Table 5-6. Most common SQLAlchemy query executors*

![Table 5-1.png](http://upload-images.jianshu.io/upload_images/134602-6f93435cd110bdbc.png)


relationship的使用跟queries的使用很类似，如下例子展现了one-to-many的relationship查询：

```
>>> users = user_role.users
>>> users
[<User u'susan'>, <User u'david'>]
>>> users[0].role
<Role u'User'>
```

执行user_role.users的时候会隐式地调用all()并返回结果，这样会导致我们无法为查询添加filtesr。这样会导致一个小问题，比如我们希望返回的users排序规则是name的字母顺序，但因为uers_role.users已经返回了查询结果所以我无法再排序。在Example 5-4中，我们通过给relationship添加了一个lazy='dynamic'的参数使得查询不会自动被执行：

```
class Role(db.Model):
    # ...
    users = db.relationship('User', backref='role', lazy='dynamic')
    # ...
```

通过上述的配置以后我们就可以给user_role.users添加filters了：

```
>>> user_role.users.order_by(User.username).all()
[<User u'david'>, <User u'susan'>]
>>> user_role.users.count()
2
```

### 在视图方法中操作数据库

前面部分的数据库操作可以直接在视图方法中使用，Example 5-5为新版本的home页面：

*Example 5-5. hello.py: Database use in view functions*


```
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''

        return redirect(url_for('index'))
    return render_template('index.html',
        form = form, name = session.get('name'), known = session.get('known', False))

```
每次用户提交name到后台应用程序会首先使用 filter_by() 去数据库查询，并且会有一个known变量被传递到前台用于format问候语。对应的模板改动 Example 5-6如下，新的模板会使用known变量来新增一条问候语，对于第一次访问和多次访问的用户问候语内容会有不同：

*Example 5-6. templates/index.html*


```
{% extends "commonBase.html" %}
{% import "bootstrap/wtf.html" as wtf %}

{% block title %}Flasky{% endblock %}

{% block page_content %}
    <div class="page-header">
        <h1>Hello, {% if name %}{{ name }}{% else %}Stranger{% endif %}!</h1>
        {% if not known %}
            <p>Pleased to meet you!</p>
        {% else %}
            <p>Happy to see you again!</p>
        {% endif %}
    </div>
    {{ wtf.quick_form(form) }}
{% endblock %}
```

你可以checkout代码到5b的历史节点执行和查看效果，确保你已经按照前一节中的db.create_all()方法生成了所需的数据库表结构。


### Model集成Python Shell


在shell中测试数据库操作，我们需要导入数据库实例db和对应的models，每次开一个新的shell都这样做未免显得繁琐了。Flask-Script的shell命令行能够配置成每次自动导入特定对象。为了把一些对象加入shell命令的导入列表，我们要给shell命令注册一个make_context的回调函数，具体如Example 5-7所示：

*Example 5-7. hello.py: Adding a shell context*

```
from flask.ext.script import Shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

manager.add_command("shell", Shell(make_context=make_shell_context))
```

make_shell_context()方法构建了数据库实例和models，所以它们都能自动被导入到shell中了：

```
>>> app
<Flask 'hello'>
>>> db
<SQLAlchemy engine='sqlite:////Users/appledev072/Documents/flasky/data.sqlite'>
>>> User
<class '__main__.User'>
```
### 使用Flask-Migrate来做数据库的Migrations

开发进行到一定阶段，你会发现model的结构需要发生改变，相应的数据库表结构也应该要更新。Flask-SQLAlchemy调用create_all()来新建表当且只发生在这些表不存在的时候，因此更新表结构的唯一办法就是先删除旧的表，当让这样不可避免地会把所有存储的数据也一并销毁了。

更好的做法是使用数据库迁移框架，就像代码版本控制工具会监控代码改动一样，一个数据库迁移框架能够跟踪数据库表的变化，并且能把新的改动应用到到旧的表中。

SQLAlchemy的开发者写了一个名叫Alembic的框架，但是在Flask中我们并不打算直接使用它，而是使用基于Alembic的扩展Flask-Migrate，这是一个轻量级的的扩展并且还和Flask-Script进行了集成，意味着你可以通过Flask-Script命令行完成所有的操作。

#### 创建迁移的资源库

首先我们先安装Flask-Migrate：

```
(venv) $ pip install flask-migrate
```

如下示例展示扩展的初始化配置：

*Example 5-8. hello.py: Flask-Migrate configuration*

```
from flask.ext.migrate import Migrate, MigrateCommand
# ...
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
```
为了将数据库迁移的命令暴露出来，我们把MigrateCommand类添加到了Flask-Script的manager对象中，在这个例子中，暴露出来的MigrateCommand命令为db。在使用数据库迁移之前，需要首先通过init命令来创建一个迁移的资源库：

```
(venv) $ python hello.py db init
      Creating directory /home/flask/flasky/migrations...done
      Creating directory /home/flask/flasky/migrations/versions...done
      Generating /home/flask/flasky/migrations/alembic.ini...done
      Generating /home/flask/flasky/migrations/env.py...done
      Generating /home/flask/flasky/migrations/env.pyc...done
      Generating /home/flask/flasky/migrations/README...done
      Generating /home/flask/flasky/migrations/script.py.mako...done
      Please edit configuration/connection/logging settings in
      '/home/flask/flasky/migrations/alembic.ini' before proceeding.
```

init命令创建了迁移的文件夹，所有迁移脚本都会被存储在这个文件件中。注：该文件夹也会被纳入到应用程序的版本控制当中，就相当于迁移资源库是一个版本控制，而整个应用是一个外设与迁移资源库的资源库。

#### 创建迁移脚本

在Alembic中，数据库迁移是通过migration脚本来完成的，这个脚本有两个方法分别叫做upgrade() 和downgrade()。upgrade()方法会把新的数据库改动作为迁移的一部分，而downgrade则移除最新的改动。通过添加和移除改动，Alembic能够配置数据库到任何历史节点上（`注`:不是很理解，难道分别对应的prev和next的操作？会退到最出事的状态岂不是要许多次的downgrade）。

Alembic迁移能够有手动和自动两种模式可用。手动的migration要创建空的工具方法upgrade()和downgrade()并通过使用Alembic提供的操作对象来自己实现，自动migration会自动查找当前数据库和model和数据库结构的不同之处。自动迁移有可能会丢失一些数据，因此Migration scripts generated automatically should always be reviewed（`注`：如何reviewed Migration scripts不是很理解）。

如下 migrate 命令创建了一个自动迁移的脚本：

```
(venv) $ python hello.py db migrate -m "initial migration"
   INFO  [alembic.migration] Context impl SQLiteImpl.
   INFO  [alembic.migration] Will assume non-transactional DDL.
   INFO  [alembic.autogenerate] Detected added table 'roles'
   INFO  [alembic.autogenerate] Detected added table 'users'
   INFO  [alembic.autogenerate.compare] Detected added index
   'ix_users_username' on '['username']'
     Generating /home/flask/flasky/migrations/versions/1bc
     594146bb5_initial_migration.py...done
```

你可以直接checkout到5d的历史节点，因为迁移脚本已经包含在代码中，上述命令你不用再自己执行一遍了。

#### Upgrading数据库


For a first migration, this is effectively equivalent to calling db.create_all(), but in successive migrations the upgrade command

一旦migration完成，你就可以通过db upgrade 来更新数据库了，你可以把data.sqlite删除以后再执行命令，你会发现删除的数据库通过migration命令重又建了。

```
(venv) $ python hello.py db upgrade
```

数据库设计和使用是非常重要的，正本书都会围绕这个主题进行，本章只是进行了总体介绍，更多相关的主题会在其他章节中介绍，下一章主题是如何发送邮件。


# 第6章 邮件


很多类型的应用程序都需要在某些事件发生的时候通知用户，其中最常用的方式是通过邮件。虽然python包smtplib能够在Flask应用程序中使用，但是基于smtplib的Flask-Mail和Flask集成会更好。`注`：本章笔记虽然做完却完全没理解为什么不用密码就能发邮件、为什么自己通过shell发送没有成功的问题，算是给自己留了一个大坑留着日后再来补充解决吧。继续向前走┏ (゜ω゜)=☞


## Flask-Mail的使用

先通过pip来安装Flask-Mail:

```
(venv) $ pip install flask-mail
```

Flask-Mail连接到一个Simple Mail Transfer Protocol (SMTP) 服务器并且将邮件交给它来发送。如果什么参数也没配置，Flask-Mail默认连接到localhost的25号端口，并且发送邮件不会有任何的身份验证。Table 6-1 显示了SMTP能够配置的参数选项列表：
*Table 6-1. Flask-Mail SMTP server configuration keys*
![Table 5-2.png](http://upload-images.jianshu.io/upload_images/134602-02e1aac7f764cd56.png)

开发时使用公共的SMTP服务器可能会更加方便，Example 6-1展示了一个如何通过Google Gmail账号来发送邮件的应用程序配置：
*Example 6-1. hello.py: Flask-Mail configuration for Gmail*

```
import os
# ...
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
```


`注`：不要把你的账号信息直接写在代码里，尤其是你希望把应用程序最终部署到外网的时候。为了保护你的账号信息，你应该从环境变量中导入它们。Example 6-2中展示了如何对Flask-Mail进行初始化：

*Example 6-2. hello.py: Flask-Mail initialization*

```
from flask.ext.mail import Mail
mail = Mail(app)
```

username和password变量应该被定义在环境变量中，Linux和Mac OS下可以可以在bash中使用如下命令进行设置：

```
(venv) $ export MAIL_USERNAME=<Gmail username>
(venv) $ export MAIL_PASSWORD=<Gmail password>
```


### 通过Python Shell发送邮件

为了测试上述配置是否有用，你可以在shell中尝试发送一封测试邮件：

配置和定义send_mail：

```
(venv) $ python hello.py shell
>>> from flask.ext.mail import Message
>>> from hello import mail
>>> msg = Message('test subject', sender='you@example.com', recipients=['you@example.com'])
>>> msg.body = 'text body'
>>> msg.html = '<b>HTML</b> body'
>>> with app.app_context():
...    mail.send(msg)
...
```

Flask-Mail的send()方法使用了current_app，因此它需要在一个激活的应用程序context中被执行。

### 邮件和应用程序集成

为了避免每次都手动创建邮件信息，我们应该把公共的部分抽象到应用程序的方法中，并且我们可以使用Jinja2模板来很便利地构建邮件的内容。例子如Example 6-3所示：


*Example 6-3. hello.py: Email support*


```
from flask.ext.mail import Message

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)

```

send_email方法依赖两个配置项，他们分别定义了主题的前缀和邮件发送者的地址，方法还有一系列参数：接收者邮件地址、主题内容、邮件模板、邮件内容参数。模板是没有后缀的名称，这样就能够有两个版本的邮件内容可共选择使用了，最终传递给render_template() 的参数kwargs将会被用来渲染邮件内容。


index()这个视图方法能够简单扩展一下使它具备只要有新用户名接收到就发送邮件给管理员的功能。Example 6-4列举了做出的修改：

```
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
#...
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''

        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))
```

邮件的接受者被存储在系统变量FLASKY_ADMIN中，两套模板文件（text和html版本的）会被存储在templates下的一个子目录中用以和其他的模板区分。你可以吧代码checkout到6a的历史节点查看。

除了最开始配置的MAIL_USERNAME 和 MAIL_PASSWORD 环境变量，我们还需要配置FLASKY_ADMIN ：

```
(venv) $ export FLASKY_ADMIN=<your-email-address>
```

在这些环境变量都被正确设置以后，我们就可以测试键入新的名字然后去邮箱查看是否收到有邮件了。

### 发送异步邮件


如果你有尝试过发送几封测试邮件，你会发现执行mail.send()被block住了，并导致浏览器这段时间内不能响应，为了避免这个浏览器延迟的问题，应该发送邮件的功能能给交给后台的线程来做，Example 6-5展示了新做的改动：

*Example 6-5. hello.py: Asynchronous email support*

```
from threading import Thread

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
```

这种实现方式突出了一个有趣的实现，很多Flask的扩展的操作都要在application和request的contexts下。Flask-Mail的send()使用了current_app，因此它要求有context是激活的。但当mail.send()方法在另一个线程中激活的时候，application context需要通过app.app_context()手动创建。


你可以checkout到6b的历史节点来执行和查看效果。现在你运行程序会发现响应好了很多，但是要记住应用程序发送大量的邮件，有一个专用的任务用来发送邮件而不是每次发送邮件都新开一个线程会更加合理。比如send_async_email() 的执行可以交给[Celery](http://www.celeryproject.org/)任务队列来做。

本章完成了一个Web应用程序所需要了解的其他知识的介绍，现在的问题是我们的hello.py脚本已经开始变得很大并且难以维护了。下一章会介绍如何构建大型应用程序的架构。


# 第7章 大型应用程序架构

把一个小应用程序的代码都放在一起会很方便，但是不利于扩展，尤其当项目开始变大时在一个文件中工作就会带来一些问题。不像其他框架，Flask应用程序没有特定的组织方式，选择权完全交给了使用者。本章会介绍一种按照包和模块来组织大型应用程序的方法，并会在本书剩余的章节都采用这种结构。


## 项目结构


Example 7-1展示了一个Flask应用程序的布局：

*Example 7-1. Basic multiple-file Flask application structure*

![Table 5-2-2.png](http://upload-images.jianshu.io/upload_images/134602-de983b9d8239d0fe.png)


顶级有四个文件夹，分别是：

- Flask应用程序所在的包通常被命名为**app**
- 数据库迁移相关的脚本被放置在**migration**
- 单元测试写在在**tests**
- **venv**包含了Python的虚拟环境

同样，增加了一些新的文件：

- requirements.txt 列举了依赖的包方便在新的电脑中对虚拟环境快速进行配置
- config.py 存储了应用程序的配置参数
- manage.py 用于启动应用程序以及做一些其他任务

为了更好地理解这样的布局方式，后面的部分会介绍如何从一个只有hello.py的程序扩展到上图所示的结构。

## 配置选项

应用程序需要一些配置，比如对于开发、测试、产品会需要不同的数据库那样才不会相互影响。和单文件版本中在hello.py中写所有的配置不同，我们能够用类层级的方式来组织配置：

*Example 7-2. config.py: Application configuration*

```
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config): DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \ 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```


Config基类包含了对所有配置通用的设置，不同的配置子类则定义了特有的设置。随需求变更还能增加其他配置子类。

为了让配置更灵活、安全，一些配置参数可以从环境变量中导入，比如SECRET_KEY考虑到安全性，可以存储在环境变量中，并且在配置脚本中提供了一个默认值以防环境变量没有设置它。

在三套不同的配置中，SQLALCHEMY_DATABASE_URI被赋予了不同的值，这样运行在三套不同配置下的应用程序都使用了不同的数据库。

配置类定义了类方法init_app()，它接受一个应用程序实例作为参数。这样特殊的配置就能够执行了（`注`：原文是 Here configuration-specific initialization can performed 没明白init_app()这个方法跟特殊配置起不起作用有什么关系，至少在本章中的例子中没有体现出来）。当前，仅Config类实现了一个空的init_app()方法。

在配置文件的底部不同的配置被添加到了字典中，并且开发环境的配置被设置成了默认的。

## 应用程序包App


应用程序包app是所有应用程序代码、模板、静态资源文件存放的地方，当然你也可以根据项目需求取别的名字。模板和资源文件的文件夹都被放入了app中，数据库对应的models和邮件支持功能模块则分别对应 app/models.py 和 app/email.py。

### 使用工厂方法来构建应用示例

在单文件版本中创建应用程序实例很方便，但是通常会有缺陷。因为应用程序实例在全局作用于下被创建，而实例被创建后是没办法动态修改配置的。 尤其在做单元测试时，因为要跑不同的数据库，所以我们要应用不同的配置。

解决办法就是通过使用工厂方法延迟应用程序实例的创建，这样不仅仅是延迟了创建时间还让脚本有创建多个应用程序实例的能力，这对于测试尤其有用。Example 7-3中在app包中定义了了这样一个工厂方法。

app包导入了Flask目前会用到的扩展，但因为应用程序实例还没有被构建出来，它们都还没有被正确初始化。create_app()这个工厂方法接受一个配置名称作为参数，通过使用Flask提供的app.config的from_object()方法，我们就能从config.py中导入所需要的配置。一旦应用程序实例被创建出来，扩展就能够通过调用init_app()来完成初始化。

*Example 7-3. app/\_\_init\_\_.py: Application package constructor*

```
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    # attach routes and custom error pages here

    return app
```
工厂方法返回的应用程序实例还不完整，因它们没有包含路由和错误处理功能，下一节会介绍如何解决这个问题。

### 使用Blueprint来实现应用程实例的功能

用工厂方法构建应用程序实例会给路由设置带来一些麻烦。单脚本应用中，应用程序实例是全局的，路由能简单地用app.route decorator来定义。但是现在应用程序实例是运行时创建的，app.route decorator只在在create_app()以后才存在，除此之外app.errorhandler decorator也有同样的问题。

Flask提供的解决方案是使用blueprints来解决这个问题。blueprints跟application类似，也能定义路由。不同之处是它的路由都处于休眠状态，直到它被注册到应用程序实例后路由才是它的一部分。

blueprint在全局作用域下使用，因此我们完全可以像在单文件中那样使用路由。当然你既能通过单文件也能通过更加组织良好的方式。为了达到最大程度的便利性，一个子包结构被创建用于管理blueprint。Example 7-4展示了在这个main包中如何创建blueprint：

*Example 7-4. app/main/__init__.py: Blueprint creation*

```
from flask import Blueprint
main = Blueprint('main', __name__)
from . import views, errors
```

blueprints被创建为Blueprint的实例对象，构造函数有两个参数：blueprint的名字和它所在的模块或者包，在这个应用程序中，Python的 \_\_name\_\_ 变量就是第二个参数所需要的值。

应用程序的路由被存储在app/main/views.py模块中， 错误处理则在app/main/errors.py。导入这些模块以后，路由和错误处理就和blueprint关联起来了。

有一点要注意路由和错误处理模块是在app/\_\_init\_\_.py的底部被导入的，因为views.py 和 errors.py要导入main blueprint，所以为了避免循环依赖我们要等到main被创建出来才能够导入路由和错误处理。
如Example 7-5所示，blueprint在create_app()方法内被注册到应用程序实例中：

*Example 7-5. app/\_\_init\_\_.py: Blueprint registration*


```
def create_app(config_name):
    # ...
    from main
    import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
```

Example 7-6展现了错误处理：

*Example 7-6. app/main/errors.py: Blueprint with error handlers*

```
from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
```


在blueprint使用错误处理，如果使用@app.errorhandler，只有由blueprint定义的路由中导致的错误才会触发对应的handler，如果想要错误处理对整个应用程序可用，我们需要使用@main.app_errorhandler。


Example 7-7展示了使用blueprint方式的路由：

*Example 7-7. app/main/views.py: Blueprint with application routes*

```
from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # ...
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())
```

在blueprint中使用视图方法跟之前有两个不同的地方。第一个是route是来自blueprint，即-使用@main.route，第二个是url_for()方法的使用。在前面介绍过url_for()的参数默认是视图方法的名称，比如在单脚本应用中index()这个视图方法的URL能够通过url_for('index')获取到。

在blueprints中区别在于所有的作用域都来自于blueprint（作用域就是blueprint的名称，即Blueprint构造函数的第一个参数），因此index()视图方法需要通过main.index来获取到URL，即url_for('main.index')。url_for()方法同样支持参数的更短形式，通过将blueprint名字省略，我们可以简写为url_for('.index')。当然如果跨越不同的blueprints，blueprint的名字还是要加上的。

为了完成应用程序，我们还需要在app/main/forms.py模块导入form相关的一些对象。

## 启动脚本

在顶层文件夹下的manage.py是用来启动application的：

*Example 7-8. manage.py: Launch script*

```
#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
```
该脚本首先创建应用程序实例，然后从系统环境中读取FLASK_CONFIG变量，如果该变量没有定义则使用默认值。然后Flask-Script, Flask-Migrate等扩展的实例都被初始化。为了方便在Unix-based系统下运行我们增加了第一行。


## Requirements文件

Applications应该包含一个requirements.txt，它记录了有着准确版本号的所有包依赖，这对以在其他电脑上初始化项目环境很重要。通过如下命令能够自动生成一个项目用到的包的requirement.txt文件：

```
(venv) $ pip freeze >requirements.txt
```

在一个新的环境中，你如果要复制虚拟环境中的安装包，只需要执行如下命令即可：

```
(venv) $ pip install -r requirements.txt
```


该书示例中的requirement.txt中的包可能有一些已经过时了，你可以选择更加新版的包。如果因此遇到了什么问题，只要回退到老版本即可，因为老版本的都是通过了测试和应用程序兼容的。

## 单元测试

到目前应用程序还很小，几乎还没有什么要测试的，但如Example 7-9所示我们先来写一个小的测试例子：

*Example 7-9. tests/test_basics.py: Unit tests*

```
import unittest
from flask import current_app
from app import create_app, db

class BasicsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
```

测试是按照Python包中的典型的单元测试的写法来构建的，setUp() 和 tearDown() 方法在每个测试方法执行前后都会运行，任何以test_ 开头的方法都会被当做测试方法来执行。关于使用Python包来做单元测试的更多信息可以查看[official documentation](http://bit.ly/py-unittest)。


setUp()方法创建了测试所需的环境， 他首先创建了应用程序实例用作测试的山下文环境，这样就能确保测试拿到current_app, 然后新建了一个全新的数据库。数据库和应用程序实例最后都会在tearDown() 方法被销毁。


第一个测试确保了应用程序实例是存在的，第二个测试应用程序实例在测试配置下运行。为了确保测试文件夹有正确的包结构，我们需要添加一个tests/\_\_init\_\_.py文件（`注`：涉及Python包相关知识），这样单元测试包就能扫描所有在测试文件夹中的模块了。

你可以把代码checkout到7a的历史节点，并且执行 `pip install -r requirements.txt` 来确保你安装了所需要的包。为了运行测试用例，还需要添加命令到manage.py中：

*Example 7-10. manage.py: Unit test launcher command*

```
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
```

manager.command decorator所对应的方法名字就是命令的名字，并且方法的文档信息会被显示在help中，test() 的实现调用了unittest package包的test runner。如下是运行过程：

```
(venv) $ python manage.py test
test_app_exists (test_basics.BasicsTestCase) ... ok
test_app_is_testing (test_basics.BasicsTestCase) ... ok
.----------------------------------------------------------------------
Ran 2 tests in 0.001s
OK
```

## 数据库设置

重构后的应用程序使用了跟单文件本版本中完全不同的数据库。数据库URL会首先从环境变量中获取，然后把默认的SQLite数据库作为备选，在三个配置环境下数据库的名字是不同的。

不论数据库的URL是什么，只要是转换到一个新的数据库数，据库表一定要被重新创建（`注`：原文Regardless of the source of the database URL, the database tables must be created for the new database 不完全理解）。使用Flask-Migrate进行迁移管理的过程中，数据库表能够通过如下命令被新建或者upgrade：
```
(venv) $ python manage.py db upgrade
```

第一部分的内容到此算是结束了，我们已经基本介绍了使用Flask来创建应用程序的所有知识，但是你也许仍旧不确定如何将他们捏合在一起。第二部分的目标就是帮助你完成一个应用程序的开发。


待解决的问题：
1. 一个翻译问题不理解
2. 一个icon不知道做什么用
3. 一个lang设置不起作用
4. 给上述笔记加图片啊
5. 数据库 rollback的功能为什么跟我们理解不一样
6. 数据库 upgrade的描述跟我理解的不一样
7. 数据库 自动迁移会有数据丢失，要review migration scripts, how?
8. 数据库 关于one-to-many的另一种实现方式的描述
9. 邮件 为什么shell发邮件能成功
10. 邮件 跟视图方法集成的例子中，只要邮箱都密码就能发送？！
11. 架构 什么叫数据库是新的，数据库表就一定会被重建，a->b->a算新的嘛？


# 第8章 用户授权

多数的应用程序都需要追踪用户身份，当用户连接到应用程序时，一个获取用户身份信息的过程就开始了，一旦应用程序知道了用户身份，它就能提供定制化的体验。通常授权都会要求用户提供唯一标识（要么是邮件要么是用户名）以及一个密码。在本章，一个完整的授权系统会被创建。

## Flask中授权相关的包和扩展


在Python中有很多用户授权的包，但这些包不会包含所有功能。本章我们会组合使用如下几个包：

- Flask-Login: 管理登陆用户的session
- Werkzeug: 密码加密和校验
- itsdangerous: 加密token的初始化和校验

除了做用户授权的这些包外，我们还会用到一些用作常规目的的扩展:

- Flask-Mail: 发送授权相关的email
- Flask-Bootstrap: HTML模板
- Flask-WTF: Web表单

## 密码安全

存储在数据库中的用户信息通常被Web应用的开发者高度重视，如果攻击者能够攻击你的服务器并获取到数据库信息，通常会使你面临着远超于想象的风险。因为多数用户在不同的站点使用同样的密码，这意味着哪怕你的站点没有存储什么有价值的信息，但是攻击者能进入和用户有关的其他站点。

密码安全的关键在于对原始密码进行加密：把用户输入的密码作为输入值，然后对输入值进行一次甚至多次加密，然后得到的新的字符序列就是真正存储的密码。因为加密算法是确定的，任何时候用户输入原密码得到的加密结果肯定是一样，这样就能够进行密码校验。

`注`：密码加密是一个复杂的任务，你最好不要自己去实现而是使用已经被开源社区很多人认定可靠的库。如果对密码加密有兴趣，[Salted Password Hashing - Doing it Right](http://bit.ly/saltedpass) 这篇文章值得一读。

### 使用Werkzeug做密码加密
Werkzeug的安全模块实现了密码加密的功能，并提供了两个方法分别用来加密和校验：
- generate_password_hash(password, method=pbkdf2:sha1, salt_length=8) 方法接收一个普通字符串作为参数，加密得到另一个用来被存储到数据库的字符串。默认的method和salt_length对多数用户来说已经能够满足要求了。

- check_password_hash(hash, password) 方法第一个参数是来自数据库的加密后的密码，第二个参数是来自用户输入的密码，校验通过返回True。

例子8-1对第五章所创建的User model做了如下改动：

*Example 8-1. app/models.py: Password hashing in User model*

```
class User(db.Model):
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
```
加密方法是一个write-only方法，用户通过调用加密的setter方法时会调用Werkzeug的generate_password_hash()，并把加密好的self.password_hash最终写到数据库中。直接读取password会报错，因为很显然一旦数据库加密完成以后，是无法在获取到原始密码串。verify_password则接收一个来自用户输入的密码用来和model中存储的password_hash进行比对，通过校验返回True。
可以把代码checkout到8a的历史节点，然后在shell执行加密和校验的方法：
```
(venv) $ python manage.py shell
>>> u = User()
>>> u.password = 'cat'
>>> u.password_hash
'pbkdf2:sha1:1000$duxMk0OF$4735b293e397d6eeaf650aaf490fd9091f928bed'
>>> u.verify_password('cat')
True
>>> u.verify_password('dog')
False
>>> u2 = User()
>>> u2.password = 'cat'
>>> u2.password_hash
'pbkdf2:sha1:1000$UjvnGeTP$875e28eb0874f44101d6b332442218f66975ee89'
```
注意，u和u2虽然密码相同，但是加密结果是不同的。我们可以把上述测试写到单元测试中，下例中我们在测试包种添加了一个新的模块，该模块有三个方法用于测试User model中做的改动：

*Example 8-2. tests/test_user_model.py: Password hashing tests*

```
import unittest
from app.models import User


class UserModelTestCase(unittest.TestCase):

    def test_password_setter(self):
        u = User(password='cat')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(password='cat')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        u = User(password='cat')
        u2 = User(password='cat')
        self.assertTrue(u.password_hash != u2.password_hash)
```

## 创建授权的Blueprint
在第七章介绍的blueprints是在应用程序实例被创建以后用来定义路由的，它的实现被移入了工厂方法中。跟用户授权相关的路由我们也可以用blueprint来做，通过对不同的系统功能使用不同的blueprint是良好的组织代码的方法。
如下例所示，我们建立了auth的包，在包中新建了了blueprint对象，并从views.py引入了路由：

*Example 8-3. app/auth/\_\_init\_\_.py: Blueprint creation*

```
from flask import Blueprint
auth = Blueprint('auth', __name__)
from . import views
```
app/auth/views.py模块导入了路由并使用它的route decorator来定义了跟授权相关的路由。如下例子中定义了一个地址为 /login 的路由：

*Example 8-4. app/auth/views.py: Blueprint routes and view functions*

```
from flask import render_template
from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')
```

注意render_template()中的模板被存放在了auth文件夹中，Flask会去应用程序下的templates中寻找对应的模板，因此auth文件夹必须是templates的子文件夹。通过给auth blueprint建立单独的文件夹，我们就能把它和main blueprint的文件区分开来避免命名之类的冲突：
`注`：blueprints当然也能为模板定义独立的文件夹，这样render_template()方法默认去templates 文件夹查询模板，查询不得之后会去其他配置文件夹中寻找。


然后auth blueprint需要被添加到create_app()的工厂方法里：

*Example 8-5. app/\_\_init\_\_.py: Blueprint attachment*

```
def create_app(config_name):
    # ...
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    return app
```
app.register_blueprint()方法中url_prefix参数是可选的，当设置了url_prefix以后，所有auth blueprint的路由都会默认加上前缀，这里前缀设置成了/auth。比如 /login 会被注册为 /auth/login，对应的完整URL是  http://localhost:5000/ auth/login。你可以checkout代码到8b的历史节点来查看代码。

## 使用Flask-Login来进行用户授权

当用户登录站点的时候授权状态应该要被记录下来用于决定跳转/获取到不同的页面， Flask-Login是一个很小但是非常有用的用户授权扩展，使用前先进行安装：
```
(venv) $ pip install flask-login
```
### 构建登陆的User Model

要和User model集成Flask-Login功能，我们需要实现如下表中的一些方法：
*Table 8-1. Flask-Login user methods*
![Table 5-3.png](http://upload-images.jianshu.io/upload_images/134602-18721f4b7f9e6f89.png)


我们可以在model中直接实现这四个方法，但是更简单的做法还是使用UserMixin类，它提供了默认的实现，如下为修改后的User model:

*Example 8-6. app/models.py: Updates to the User model to support user logins*

```
from flask.ext.login import UserMixin
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
```
注意我们添加了一个email属性，因为用户可能忘记用户名，但通常不忘记邮件地址。为了初始化Flask-Login，还要在应用程序的工厂方法中添加一些内容：
*Example 8-7. app/\_\_init\_\_.py: Flask-Login initialization*
```
from flask.ext.login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    # ...
   login_manager.init_app(app)
    # ...

```
session_protection属性可以设置None, basic, strong, 设置为strong的时候Flask-Login 会监控用户的IP地址变动并提示用户重新登陆。login_view属性设置了login页面的断点（注：本书很喜欢用endpoint这个词汇，实在想不到合适的翻译，其实就是模块位置的一个表示），之所要指定auth的前缀是因为它在auth blueprint中。

最后程序还需要查询用户信息的方法：

*Example 8-8. app/models.py: User loader callback function*

```
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
```

用户查询方法返回了接收一个被当做Unicode字符串用户标识，返回一个用户对象或None。

### 保护路由
为了保证某些链接只能被已经登陆过的用户访问到，Flask-Login提供了login_required decorator，如果一个没有授权的用户访问到这里，Flask-Login会终止请求然后跳转到登陆页面去：

```
from flask.ext.login import login_required
@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'
```

### 添加登陆表单


登陆表单会为email地址构建一个text field，一个password field, 一个“remember me”的checkbox，一个submit button。Flask-WTF form如下所示：

*Example 8-9. app/auth/forms.py: Login form*

```
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email
class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
```

email field使用了WTForms提供的Length()和Email()校验器。PasswordField 展现了一个type="password"的输入框。Boolean Field显示了一个checkbox。相关的模板被存储在auth/login.html，只需要Flask-Bootstrap’s wtf.quick_form() 就能进行绘制。下图展现了绘制出来的登陆界面效果：


![Table 5-5.png](http://upload-images.jianshu.io/upload_images/134602-2cc334829920a764.png)

*Figure 8-1. Login form*

base.html模板中的导航栏显示 "Sign In" 还是 "Sign Out" 可以用Jinjia2的条件判定当前用户是否存在：

*Example 8-10. app/templates/base.html: Sign In and Sign Out navigation bar links*

```
<ul class="nav navbar-nav navbar-right">
    {% if current_user.is_authenticated() %}
    <li><a href="{{ url_for('auth.logout') }}">Sign Out</a></li> {% else %}
    <li><a href="{{ url_for('auth.login') }}">Sign In</a></li> {% endif %}
</ul>

```

current_user变量是被Flask-Login定义的对象，能够在视图方法和模板中自动获取它。变量包含了当前登录用户的信息，或者一个代理匿名用户对象。  代理匿名用户对象调用is_authenticated()方法会返回False，这样就很好判定用户是否登陆过了。

### 用户登入

login()视图方法的实现如下例所示：

*Example 8-11. app/auth/views.py: Sign In route*
```
from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user
from . import auth
from ..models import User
from .forms import LoginForm
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)
```

视图方法像第四章所做的那样创建了一个LoginForm对象。当请求是GET类型时，直接渲染带登陆表单的模板，当请求为POST类型，首先使用Flask-WTF的validate_on_submit()方法校验输入值，然后尝试登入用户。

登入的逻辑首先检查表单数据中是否包含邮件地址，如果包含则结合用户密码来调用verify_password()方法判定用是否存在。如果用户密码正确，Flask-Login的login_user() 方法会被调用，然后记录下登陆用户的信息。

login_user()方法会传入一个“remember me” Boolean的参数，意味着用户在表单上没勾选，那么user session当浏览器窗口被关闭的时候就会失效，用户下次进入页面的时候还需要再次登入；反之则会有一个长效的cookie被设置在用户浏览器端，通过使用cookie用户的session就能够被被重新获取到（注：原书用的restored ）。

依据第四章介绍的 Post/Redirect/Get 策略，POST请求都会被重置成为GET类型的请求，但是目前例子中有两个目标地址选择。如果用户因为没有授权而跳转到的登入界面，那么之前的地址会被记录下来并存储在request.args字典的next参数中；如果没有找到的next地址，则默认跳转到首页。

如果用户输入的邮箱或者密码非法，flash message会被传递给前台用于显示。

相应的登入模板页也要进行改动，如下：

*Example 8-12. app/templates/auth/login.html: Render login form*

```
{% extends "base.html" %}
{% import "bootstrap/wtf.html" as wtf %}
{% block title %}Flasky - Login{% endblock %}

{% block page_content %}
<div class="page-header">
    <h1>Login</h1>
</div>
<div class="col-md-4">
    {{ wtf.quick_form(form) }}
</div>
{% endblock %}
```
### 用户登出

登出的路由配置如下例所示：
*Example 8-13. app/auth/views.py: Sign Out route*

```
from flask.ext.login import logout_user, login_required

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
```

用户登出需要调用Flask-Login的logout_user()方法来移除和重置users session，完成后flash了一个消息给前台，然后跳转到了home页面。

你可以checkout代码到8c的节点。代码包含了数据库迁移的脚本，你需要执行 `python manage.py db upgrade`来更新数据库。为了确保所有的依赖被正确安装了需要运行`pip install -r requirements.txt`。


### 测试登陆功能
为了测试登陆功能是否工作，home页面进行了修改，对已经登陆的用户显示用户名：

*Example 8-14. app/templates/index.html: Greet the logged-in user*

```
Hello,
{% if current_user.is_authenticated() %}
    {{ current_user.username }}
{% else %}
    Stranger
{% endif %}!
```
在模板中，current_user.is_authenticated()被用于判定用户是否登入。因为用户注册功能还没做，所以新用户只能通过shell进行创建：

```
(venv) $ python manage.py shell
>>> u = User(email='john@example.com', username='john', password='cat')
>>> db.session.add(u)
>>> db.session.commit()
```

用户创建成功以后就能登入了，如下显示了登入后的home页面：
![Table 5-6.png](http://upload-images.jianshu.io/upload_images/134602-1416159210e47a64.png)

*Figure 8-2. Home page after successful login*

注：因为Mac上默认安装的Python版本是2.7.7，测试时报错`'unicode' does not have the buffer interface`，参考 https://github.com/miguelgrinberg/flasky/issues/17 重新下载安装了[Python2.7.6](https://www.python.org/download/releases/2.7.6/)的版本后问题得到解决。

## 新用户注册


新用户想要使用应用程序必须通过注册，在注册界面用户需要输入邮件地址、用户名、密码来完成注册。

### 添加注册表单

*Example 8-15. app/auth/forms.py: User registration form*

```

class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                           Email()])
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
```


form使用了WTForms的Regexp校验器确保用户名只包含字母、数字、下划线。其他两个参数为是否匹配的标志以及不匹配时所显示的message内容。

密码需要输入两次，我们使用了WTForms的EqualTo来保证两次输入的密码是一致的。form还有两个自定义的校验器，当表单定义 validate_attributename的方法时，方法会默认被用用到对应属性attributename上，在本例中，两个自定义的校验器方法需要确保用户输入的用户名和邮箱没有跟数据库已经存在的记录冲突。否则就直接抛出一个ValidationError的错误。

模板存放在/templates/auth/register.html，内容跟 login的模板类似同样调用wtf.quick_form()来绘制表单，注册页面的效果图如下：

![Table 6-1.png](http://upload-images.jianshu.io/upload_images/134602-c256fc7f192d4d8c.png)


*Figure 8-3. New user registration form*

对于没有注册过的用户，我们需要在登陆页面给出跳转到注册页面的链接：

*Example 8-16. app/templates/auth/login.html: Link to the registration page*

```
<p>
    New user?
    <a href="{{ url_for('auth.register') }}">Click here to register</a>
</p>
```
### 注册新用户

当注册表单被提交并通过校验后，一个新用户会被加入到数据库中，注册的视图方法如下：

*Example 8-17. app/auth/views.py: User registration route*

```
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
```

你可以checkout到8d的历史节点查看和执行注册功能。

## 账号确认

对于一些类型的应用程序，确认用户信息合法是非常重要的，比如用户提供的邮件地址必须是合法有效的。为了验证邮件地址，应用程序在用户注册以后马上会发送一封邮件给用户。在用户进入邮箱点击确认的链接操作之前用户是一个未通过校验的用户。通常链接中包含了一个用于确认用户的token。

### 使用itsdangerous来初始化确认的token

最简单的账号确认方法 是在邮件中包含形如 http://www.example.com/auth/confirm/\<id\> 的地址，其中id是用户在数据库中id。当用户点击链接地址，视图方法会处理接收到的用户id然后更新该用户的状态。

但显然这不是一种安全的做法，因为任何注册用户只要知道了链接地址的规则就可以发送很多账号确认的请求，只需要在对应的URL中把id替换为随机的数字。

理想的做法是替换id为加密过的token。
第四章曾使用加密过的Cookie来确保用户Session中的内容不被篡改，这些安全Cookie是由itsdangerous这个包生成的，同样它也能被用于确认token的生成。

如下例子使用了itsdangerous来初始化一个包含了用户信息的安全token：

```
(venv) $ python manage.py shell
>>> from manage import app
>>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
>>> s = Serializer(app.config['SECRET_KEY'], expires_in = 3600)
>>> token = s.dumps({ 'confirm': 23 })
>>> token
'eyJhbGciOiJIUzI1NiIsImV4cCI6MTM4MTcxODU1OCwiaWF0IjoxMzgxNzE0OTU4fQ.ey ...'
>>> data = s.loads(token)
>>> data
{u'confirm': 23}
```

Itsdangerous提供了一些初始化token的方法，其中TimedJSONWebSignatureSerializer类能够初始化包含了失效时间的JSON Web Signatures (JWS)。

dumps()方法通过传递进来的参数生成了一个加密的签名然后把结果序列化为一个token字符串，其中失效时间是以秒来计算的。

为了解密这个token，序列化对象提供了一个loads()方法它只接受token作为唯一的参数，并且会确认签名和失效时间，如果合法会返回原来加密前的数据，否则当token不合法或者已经失效则会抛出一个错误。


token的初始化和确认都能在User model中被使用，如下例子所示：

*Example 8-18. app/models.py: User account confirmation*

```
class User(UserMixin, db.Model):
    # ...
    confirmed = db.Column(db.Boolean, default=False)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True
```
generate_confirmation_token()方法初始了一个包含默认失效时间的token，confirm() 方法会校验token的合法性并设置新增加的属性confirmed的值。

confirm() 方法除了校验token的值，还对校验得出的数据中的id和已经登录用户的id进行比对，这就确保了一点：就算你能够format一个正确的token，你仍旧没法保证该token跟已经登录的用户是匹配的。

注：因为model中增加了新的属性，数据库迁移需要被重新应用一下。


上面介绍的两个方法很容易在单元测试中使用，具体可见项目代码的测试部分。

### 发送确认的Email

我们要在注册成功跳转到/index之前用户发送一封确认邮件，如下是对代码进行的改动：

*Example 8-19. app/auth/views.py: Registration route with confirmation email*

```
from ..email import send_email

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # ...
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account',
                   'auth/email/confirm', user=user, token=token)
        flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

```

尽管我们在应用程序中配置了每个请求结束后自动commit数据库改动，但是因为我们要发送包含有效用户信息的邮件（其中包含id值），所以必须要在发送之前进行commit。

授权的blueprint要用到的邮件模板被存放在了 templates/auth/email下面，第六章有介绍过每一个邮件模板都有plain 和 rich-text 两种格式。比如Example 8-20显示了plain-text 格式的邮件模板，HTML版本的可以在项目资源库中找到：

*Example 8-20. app/auth/templates/auth/email/confirm.txt: Text body of confirmation email*

```
Dear {{ user.username }},
Welcome to Flasky!

To confirm your account please click on the following link:
{{ url_for('auth.confirm', token=token, _external=True) }}
Sincerely,
The Flasky Team
Note: replies to this email address are not monitored.
```

默认地url_for()会初始化一个相对的URL，比如 url_for('auth.confirm', token='abc') 会返回 '/auth/confirm/abc'，当然我们在邮件中发送这样的地址肯定是不符合要求的。
因为我们在自己应用程序的上下文中使用相对地址，最后都会默认加上hostname和port，但是当做邮件内容以后，就没有这个上下文了，因此必须要给url_for()加上_external=True，这样就会返回一个信息安全的地址。

视图方法中会这样使用账号确认功能：

*Example 8-21. app/auth/views.py: Confirm a user account*


```
from flask.ext.login import current_user

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return  redirect(url_for('main.index'))
```

确认的token使用了login_required decorator，当用户点击了确认邮件中的地址以后会先要求进行登录。方法首先检查了登录用户是否已经确认过，如果已经确认过就直接跳转到home页面去。显然这样能够防止用户多次点击并跳转进入该地址。

因为token的校验都是在User model中做到的，我们需要在视图方法中调用它，并通过flash给前台传递校验的结果。但校验通过，User model
的confirmed 属性会被设置为True并且该用户会被要存到session中。

没有通过校验的用户能做什么，每个应用程序都有自己的策略。其中一种策略就是允许未确认的用户登陆，但是在校验完成之前只给她们访问用于确认账号的界面。


我们可以使用Flask的钩子 before_request hook来完成这样的功能，通过blueprint设置的钩子，before_request也只对属于blueprint的路由管用：

*Example 8-22. app/auth/views.py: Filter unconfirmed accounts in before_app_request handler*

```
@auth.before_app_request
def before_request():
    if current_user.is_authenticated() \
            and not current_user.confirmed \
            and request.endpoint[:5] != 'auth.':
        return redirect(url_for('auth.unconfirmed'))

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous() or current_user.confirmed:
        return redirect('main.index')
    return render_template('auth/unconfirmed.html')
```

before_app_request中的处理值当如下三个条件满足的时候会执行：
（1）用户已经登录过
（2）用户还没有完成校验
（3）请求的endpoint是跟auth无关的
当上述三个条件都满足以后，请求会跳转到一个名为unconfirmed.html的页面。


![Table 8-1.png](http://upload-images.jianshu.io/upload_images/134602-2cef5c91d8485877.png)


*Figure 8-4. Unconfirmed account page*

如Figure 8-4所示的unconfirmed.html中，给出了一些指导信息，并给除了一个再次发送确认邮件的链接地址。发送确认邮件的视图方法如下所示：

*Example 8-23. app/auth/views.py: Resend account confirmation email*

```
@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account',
               'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('main.index'))

```

这里的逻辑跟注册成功以后的逻辑一样，区别在于直接使用已经登录成功的用户的信息。同样的，我们也给这个路由加上了@login_required的条件，确保每次重新发送确认信息的时候用户已经登录过。

你可以把代码checkout到8e的历史节点，并且记得执行`python manage.py db upgrade`来更新数据库。

## 账号管理

随着时间的推移，用户可能会生出一些改变账号信息的需求。这些功能会在本章的示例代码中依次被加入：

### 密码修改

对安全要求比较很高的用户可能会定期对密码进行修改，这个功能比较容易实现，因为我们只需要给登录后的用户提供修改的表单，然后替换数据库的旧密码即可。可以checkout到8f的历史节点中来执行和查看效果。

### 密码重置

为了是忘记密码的用户也能正常使用应用程序，我们应该提供密码重置的功能。跟身份校验一样，我们会通过发送一封邮件给用户（邮件中包含有带token的链接），用户通过点击该链接，通过后台校验后就可以跳转到重置密码的界面。你可以checkout到8g的历史节点。

### 修改邮箱

应该给用户提供一个修改注册邮箱的功能，但是新邮箱生效之前，我们仍然需要用之前的邮箱进行确认。为了是现在这个功能，用户需要在表单中输入新的邮箱地址，然后一个带token的链接地址会发送给新的邮箱地址。当用户点击改地址，后台通过校验后，邮件就更新成功了。注：原文不大理解 While the server waits to receive the token, it can store the new email address in a new database field reserved for pending email addresses, or it can store the address in the token along with the id。你可以checkout到8h的历史节点执行和查看效果。

在下一章中，Flasky的用户子系统会开始对用户角色进行管理。

问题：
1. 为什么要设置@property，作用是什么？
2. 如何更数据库去关联起来的。
3. 测试用例如何写的。如何运行的。
4. 工厂方法流程
5. blueprint
6. 环境归环境？代码归代码？安装的package属于环境？