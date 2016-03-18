<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [项目环境](#%E9%A1%B9%E7%9B%AE%E7%8E%AF%E5%A2%83%EF%BC%9A)
- [Ruby项目的包管理历史简述](#ruby%E9%A1%B9%E7%9B%AE%E7%9A%84%E5%8C%85%E7%AE%A1%E7%90%86%E5%8E%86%E5%8F%B2%E7%AE%80%E8%BF%B0)
  - [RubyGem：解决不同版本gem包的安装和维护](#rubygem%EF%BC%9A%E8%A7%A3%E5%86%B3%E4%B8%8D%E5%90%8C%E7%89%88%E6%9C%ACgem%E5%8C%85%E7%9A%84%E5%AE%89%E8%A3%85%E5%92%8C%E7%BB%B4%E6%8A%A4)
  - [Bundle：解决配置以及相互的依赖关系](#bundle%EF%BC%9A%E8%A7%A3%E5%86%B3%E9%85%8D%E7%BD%AE%E4%BB%A5%E5%8F%8A%E7%9B%B8%E4%BA%92%E7%9A%84%E4%BE%9D%E8%B5%96%E5%85%B3%E7%B3%BB)
  - [rvm：解决将各个项目的gem环境隔离开来](#rvm%EF%BC%9A%E8%A7%A3%E5%86%B3%E5%B0%86%E5%90%84%E4%B8%AA%E9%A1%B9%E7%9B%AE%E7%9A%84gem%E7%8E%AF%E5%A2%83%E9%9A%94%E7%A6%BB%E5%BC%80%E6%9D%A5)
- [问题解答](#%E9%97%AE%E9%A2%98%E8%A7%A3%E7%AD%94)
- [参考链接](#%E5%8F%82%E8%80%83%E9%93%BE%E6%8E%A5%EF%BC%9A)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

#关于rvm, gem, bundle的理解

项目开发过程中，环境配置过程会出现包安装的问题，所以整理这篇笔记以方便理解（毕竟非ruby系程序员，看个大概，未必完全准确）。

## 项目环境

先从项目配置的过程开始讲起，配置文档中两个关键步骤分别是

```
bundle install --path vendor
```


这个步骤大概做了如下几个事情

1. 解析项目下面的Gemfile或者Gemfile.lock，构建得到包的依赖关系
2. 去服务器上下载对应的gem包到vendor文件夹下
3.  本地生成 .bundle/config文件，指定默认运行所引用的包的位置


```
bundle exec rails s
```

按照上一步骤已经在项目根目录下生成了 .bundle/config，里面配置了在什么位置去找gem包，因此只要bundle intall过程成功了，执行基本上就不会有包的问题发生了。


## Ruby项目的包管理历史简述


### RubyGem：解决不同版本gem包的安装和维护

通过使用 `gem`命令，可以很简单地装多个版本的 gem 包，比如：

```
gem install rails -v 4.1
gem install rails -v 4.2
gem install rails -v 5.0
```

### Bundle：解决配置以及相互的依赖关系

不同的人运行一个项目，要严格按照要求去安装相应版本的gem包。但是如果有人为了自己新项目升级了某个gem包，可能导致老项目不能运行，为了老项目运行，可能要求去更新别gem包到新版本才行。也就说，你得手动管理和维护每个项目的包，以及包之间的依赖关系，bundle解决的就是这么一个问题。你只需要告诉你所需要的环境，然后bundle install会根据Gemfile去计算出依赖的包结构，写入到Gemfile.lock中，并以此为依据去下载对应的版本。

在bundle install了以后，我们是能够让代码依赖正确的包去运行项目的。但是同样会遇到问题，不同的项目依赖不同，虽然省去了手动管理版本之间关系的问题，却仍旧有可能导致混用同一个包，还是会相互影响。

### rvm：解决将各个项目环境隔离开来


rvm的最基本的功能是能够进行ruby的多版本的管理和切换。如下为基本用法：

```
# 列出已知的ruby版本
rvm list known

# 安装一个ruby版本
rvm install 1.9.3

# 使用一个ruby版本
rvm use 1.9.3

# 如果想设置为默认版本，可以这样
rvm use 1.9.3 --default

# 查询已经安装的ruby
rvm list

# 卸载一个已安装版本
rvm remove 1.9.2
```

rvm更重要的作用是进行gemset的管理。假定每个项目是一个gemset，每个gemset是基于特定版本的ruby环境下的。比如ruby有两个版本1.9.2和1.8.7，我们给iVantage项目建立环境配置的过程如下：

```
rvm install 1.9.3
rvm use 1.9.3
rvm gemset create iVantage
rvm use 1.9.3@iVantage
```

通过执行如上命令，我们相当于把ruby限定在了1.9.3这个版本，而其他的gem都会被安装在一个以iVantage命名的空间内。

同样但我需要新建另外一个项目hd-wall时候，也可以如下命令：

```
rvm install 1.9.3
rvm use 1.9.3
rvm gemset create hd-wall
rvm use 1.9.3@hd-wall
```

在我们设置好ruby和项目的gemset以后，通过`bundle install`命令就可以把所有依赖的gem install到该命名空间下（比如1.9.3@hd-wall）。执行`bundle exec`的话，猜测会通过修改$PATH指向路径或者配置文件，然项目默认以该空间下的各个版本来运行。

## 问题解答

问：为什么本地成功按照文档步骤运行过iVantage，在克隆riskgod/iVantage的代码，不能直接通过`bundle exec rails s`来运行，包不是都已经安装配置过了么？

```
ytang048mac:iVantage appledev072$ bundle exec rails -s
Could not find rake-10.1.0 in any of the sources
Run `bundle install` to install missing gems.
```

答：以个人为例，之前所有的包都是通过bundle install来（1）安装gem在项目根目录下的vendor中的 （2）通过新增`.bundle/config`来增加默认的bundle exec的寻址配置（通过编辑`.gitignore`让 `vendor/` 和 `.bundle/` 显示出来可以判定这一点）。

在克隆代码后，直接执行`bundle exec rails s`首先会默认从当前目录去找`.bundle/config`, 没找到以后回去系统中安装的目录下找对应的gem，没找到以后会报错。所以解决办法有两个，一是按照要求在进行 `bundle install --path vendor` 命令，再次将包安装在 vendor中。二是通过rvm进行项目gemset的环境和切换，然后在通过bundle install来安装对应的gem到项目空间中。

两种做法孰优孰劣，个人权衡。


## 参考链接

- [https://ruby-china.org/topics/576](https://ruby-china.org/topics/576)

- [https://ruby-china.org/topics/28453](https://ruby-china.org/topics/28453)

