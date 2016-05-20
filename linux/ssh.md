# Linux SSH 編

　SSH (Secure Shell) とはクライアントとサーバ間の通信を暗号化するプロトコルのこと．以下のコマンドでサーバに接続することが出来る．デフォルトポート番号や PW 認証を利用している場合，オプション `-i` や `-p` は省略できる．

```
ssh -i ~/.ssh/id_rsa -p <port> <user>@<host>
```


## Settings

　`/etc/ssh/sshd_config` を編集する（要管理者権限）．

### Port 番号の変更

　13 行目．`<port>` は 49513 - 65535 の中から自由に選択してよい．

- 変更前

```
#Port 22
```

- 変更後

```
Port <port>
```

### root での SSH 接続の禁止

　42 行目．

- 変更前

```
#PermitRootLogin yes
```

- 変更後

```
PermitRootLogin no
```

### PW 認証の禁止

　66 行目．これで総当たり攻撃を回避できる．

- 変更前

```
PasswordAuthentication yes
```

- 変更後

```
PasswordAuthentication no
```

### SSH Server の再起動

```
# /etc/rc.d/init.d/sshd restart
```

## SCP (Secure Copy)

　SSH を介してファイルコピーを行うコマンドのこと．UNIX の標準コマンドである `cp` とほぼ同じ感覚で扱うことが出来る．

- ローカルからリモートへの転送

```
$ scp -P <port> -i ~/.ssh/id_rsa ~/foo.txt <user>@<host>:~/Desktop/
```

- リモートからローカルへの転送

```
$ scp -P <port> -i ~/.ssh/id_rsa <user>@<host>:~/bar.txt ~/Desktop/ 
```

## Public Key Authentication

### クライアント側の手順

　秘密鍵 `id_rsa` と公開鍵 `id_rsa.pub` のペアを作成する．passphrase の入力を二回ほど求められるが，空で構わない．


```
$ ssh-keygen -t rsa -f ~/.ssh/id_rsa
```

　公開鍵をサーバへ転送する．この際，一時的に PW 認証を許可する必要がある．

```
$ scp -P <port> ~/.ssh/id_rsa.pub <user>@<host>:~/id_rsa.pub.tmp
```

　後に `~/.ssh/config` を作成すると，`$ ssh example` で簡単にサーバに接続することが出来る．

```~/.ssh/config
Host example
    HostName <host>
    User <user>
    Port <port>
    IdentityFile ~/.ssh/id_rsa
```

### サーバ側の手順

　転送された公開鍵の内容を `.ssh/authorized_keys` に追記する．

```
$ mkdir .ssh
$ cat ~/id_rsa.pub.tmp >> ~/.ssh/authorized_keys
$ rm ~/id_rsa.pub.tmp
```

　`.ssh` と `.ssh/authorized_keys` のアクセス権を変更する．

```
$ chmod 700 ~/.ssh
$ chmod 600 ~/.ssh/authorized_keys
```