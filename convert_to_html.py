import markdown
from pygments.formatters import HtmlFormatter

# Markdownファイルを読み込む
with open('Flask_Tutorial_Complete.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Markdown拡張機能を設定
md = markdown.Markdown(extensions=[
    'fenced_code',
    'codehilite',
    'tables',
    'toc',
    'nl2br',
    'attr_list'
])

# HTMLに変換
html_content = md.convert(md_content)

# Pygmentsのスタイルシートを取得
formatter = HtmlFormatter(style='monokai')
styles = formatter.get_style_defs('.codehilite')

# 完全なHTMLドキュメントを作成
html_document = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Flask 完全チュートリアル</title>
    <style>
        /* リセットCSS */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        /* 基本スタイル */
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', 'Yu Gothic', 'Meiryo', sans-serif;
            line-height: 1.8;
            color: #333;
            background-color: #f5f5f5;
            padding: 0;
            margin: 0;
        }}
        
        /* コンテナ */
        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
            background-color: white;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            min-height: 100vh;
        }}
        
        /* 見出し */
        h1 {{
            color: #2c3e50;
            margin: 2rem 0 1rem 0;
            padding-bottom: 0.5rem;
            border-bottom: 3px solid #3498db;
            font-size: 2.5rem;
        }}
        
        h2 {{
            color: #34495e;
            margin: 2rem 0 1rem 0;
            padding-bottom: 0.3rem;
            border-bottom: 2px solid #ecf0f1;
            font-size: 2rem;
        }}
        
        h3 {{
            color: #34495e;
            margin: 1.5rem 0 0.5rem 0;
            font-size: 1.5rem;
        }}
        
        h4 {{
            color: #34495e;
            margin: 1rem 0 0.5rem 0;
            font-size: 1.2rem;
        }}
        
        /* 段落 */
        p {{
            margin: 1rem 0;
            text-align: justify;
        }}
        
        /* リスト */
        ul, ol {{
            margin: 1rem 0;
            padding-left: 2rem;
        }}
        
        li {{
            margin: 0.5rem 0;
        }}
        
        /* コードブロック */
        pre {{
            background-color: #272822;
            border-radius: 5px;
            padding: 1rem;
            overflow-x: auto;
            margin: 1rem 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }}
        
        code {{
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', 'Consolas', monospace;
            font-size: 0.9rem;
        }}
        
        /* インラインコード */
        p code, li code {{
            background-color: #f4f4f4;
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            color: #e74c3c;
            font-size: 0.85rem;
            border: 1px solid #ddd;
        }}
        
        /* テーブル */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        
        th {{
            background-color: #3498db;
            color: white;
            padding: 0.75rem;
            text-align: left;
            font-weight: bold;
        }}
        
        td {{
            padding: 0.75rem;
            border-bottom: 1px solid #ecf0f1;
        }}
        
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        
        /* リンク */
        a {{
            color: #3498db;
            text-decoration: none;
            border-bottom: 1px dotted #3498db;
            transition: color 0.3s;
        }}
        
        a:hover {{
            color: #2980b9;
            border-bottom-style: solid;
        }}
        
        /* 引用 */
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 1rem;
            margin: 1rem 0;
            color: #666;
            background-color: #f9f9f9;
            padding: 1rem;
            border-radius: 0 5px 5px 0;
        }}
        
        /* 水平線 */
        hr {{
            border: none;
            height: 1px;
            background-color: #ecf0f1;
            margin: 2rem 0;
        }}
        
        /* 目次 */
        .toc {{
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            padding: 1.5rem;
            margin: 2rem 0;
            border-radius: 5px;
        }}
        
        .toc ul {{
            list-style: none;
            padding-left: 1rem;
        }}
        
        .toc > ul {{
            padding-left: 0;
        }}
        
        .toc li {{
            margin: 0.3rem 0;
        }}
        
        .toc a {{
            color: #34495e;
            border: none;
        }}
        
        .toc a:hover {{
            color: #3498db;
        }}
        
        /* レスポンシブ */
        @media (max-width: 768px) {{
            .container {{
                padding: 1rem;
            }}
            
            h1 {{
                font-size: 2rem;
            }}
            
            h2 {{
                font-size: 1.5rem;
            }}
            
            h3 {{
                font-size: 1.2rem;
            }}
            
            pre {{
                padding: 0.5rem;
                font-size: 0.8rem;
            }}
        }}
        
        /* 印刷用スタイル */
        @media print {{
            body {{
                background-color: white;
            }}
            
            .container {{
                box-shadow: none;
                max-width: 100%;
            }}
            
            pre {{
                page-break-inside: avoid;
            }}
        }}
        
        /* シンタックスハイライト (Pygments) */
        {styles}
        
        /* コードブロックの追加スタイル */
        .codehilite {{
            background-color: #272822;
            border-radius: 5px;
            padding: 1rem;
            overflow-x: auto;
            margin: 1rem 0;
        }}
        
        .codehilite pre {{
            margin: 0;
            padding: 0;
            background-color: transparent;
            box-shadow: none;
        }}
        
        /* スクロールバーのスタイル */
        ::-webkit-scrollbar {{
            width: 10px;
            height: 10px;
        }}
        
        ::-webkit-scrollbar-track {{
            background: #f1f1f1;
        }}
        
        ::-webkit-scrollbar-thumb {{
            background: #888;
            border-radius: 5px;
        }}
        
        ::-webkit-scrollbar-thumb:hover {{
            background: #555;
        }}
        
        /* バッジスタイル */
        .badge {{
            display: inline-block;
            padding: 0.25rem 0.5rem;
            font-size: 0.75rem;
            font-weight: bold;
            line-height: 1;
            color: #fff;
            background-color: #3498db;
            border-radius: 0.25rem;
            margin: 0 0.25rem;
        }}
        
        /* アラートボックス */
        .alert {{
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 5px;
            border-left: 4px solid;
        }}
        
        .alert-info {{
            background-color: #e3f2fd;
            border-left-color: #2196f3;
            color: #1565c0;
        }}
        
        .alert-warning {{
            background-color: #fff3cd;
            border-left-color: #ffc107;
            color: #856404;
        }}
        
        .alert-danger {{
            background-color: #f8d7da;
            border-left-color: #dc3545;
            color: #721c24;
        }}
        
        /* ナビゲーション */
        .nav {{
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: white;
            padding: 1rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        
        .nav a {{
            display: block;
            margin: 0.5rem 0;
            color: #34495e;
            border: none;
        }}
        
        .nav a:hover {{
            color: #3498db;
        }}
        
        /* フッター */
        .footer {{
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #ecf0f1;
            text-align: center;
            color: #7f8c8d;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        {html_content}
        <div class="footer">
            <p>Python Flask 完全チュートリアル - Generated with Python Markdown</p>
        </div>
    </div>
</body>
</html>"""

# HTMLファイルとして保存
with open('Flask_Tutorial_Complete.html', 'w', encoding='utf-8') as f:
    f.write(html_document)

print("HTMLファイルが正常に作成されました: Flask_Tutorial_Complete.html")