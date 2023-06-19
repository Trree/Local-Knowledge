# 基于ChatGPT的本地知识库

## 介绍

🤖支持本地知识库,向量模型和️llm默认都是使用openai,
向量数据为[milvus](https://github.com/milvus-io/milvus),
支持上传文件和查询结果


## 使用场景
- 支持建立自己的知识库的整理和搜索
- 支持通过 prompt 搜索得到自己的文本


### 需求
- [x] 自定义大小切分文本
- [x] 通过文本建立文本向量库
- [x] 支持各种开源向量数据库
- [x] 支持页面搜索
- [ ] 支持通过 ChatGPT 优化文本
- [ ] 支持 ChatGPT 翻译自定义文本为其他语言
- [ ] 支持监督调整

### 依赖

- python = 3.10
- milvus
- openai

## 本地部署

### 1. 设置环境
```shell
# you can use conda to install the environment
$ conda create -p /your_path/env_name python=3.10
# Activate the environment
$ source activate /your_path/env_name
# Deactivate the environment
$ source deactivate /your_path/env_name
# Remove the environment
$ conda env remove -p  /your_path/env_name
```

* Project dependencies

```shell
# Clone the repository
$ git clone https://github.com/Trree/Local-Knowledge.git

$ cd Local-Knowledge
# Install dependencies
$ pip install -r requirements.txt
```

### 2.部署 Milvus

  - [milvus免费试用](https://cloud.zilliz.com/login?redirect=/projects/MA==/databases)
  - [docker本地快速部署](https://milvus.io/docs/v2.0.x/install_standalone-docker.md)


### 3. 配置

1. 在根目录找到名为 `.env.template` 的文件。由于点前缀，在某些操作系统中，默认情况下该文件可能是隐藏的。要显示隐藏文件，
  请按照您特定操作系统的说明进行操作:Windows, macOS。
2. 创建 `.env.template` 的副本，并将其命名为 `.env`；如果您已经在命令提示符/终端窗口中：`cp .env.template .env`。
3. 使用文本编辑器打开 `.env` 文件。
4. 找到一行上写着 `OPENAI_API_KEY=` 的内容。
5. 在 `=` 之后，输入您的独特的OpenAI API密钥，不要加任何引号或空格。
6. 请提供您想要使用的 `Milvus` 密钥和连接服务。
7. 保存并关闭 `.env` 文件。

### 启动服务

- 运行 `python app.py`.
- 浏览器中输入 `127.0.0.1:5000` 