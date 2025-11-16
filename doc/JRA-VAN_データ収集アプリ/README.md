# JRA-VAN データ収集アプリ

1. [1. 技術](#1-技術)
   1. [1.1. 外部ツール](#11-外部ツール)
2. [2. UI](#2-ui)
3. [3. 設計](#3-設計)
   1. [3.1. データ収集](#31-データ収集)

## 1. 技術

* 言語
  * Python
* デスクトップフレームワーク
  * Flet
  * Flet-desktop
* データベース
  * PostgreSQL

### 1.1. 外部ツール

* JRA-VAN DataLab
  * PCKEIBA

## 2. UI

## 3. 設計

### 3.1. データ収集

```mermaid

sequenceDiagram
    actor User
    participant APP as DesktopApp
    participant PM as PythonModule
    participant DB as PostgreSQL
    participant LF as LocalFile

    User ->> APP: 起動
    APP ->> User: 初期画面
    User ->> APP: 検索項目を入力<br>CSV出力
    APP ->> PM: 検索項目を渡す
    PM ->> PM: SQL文を作成する
    PM ->> DB: SQLで検索する
    DB ->> PM: データを返却する
    PM ->> LF: CSVで出力する
    PM ->> User: 完了を通知する

```
