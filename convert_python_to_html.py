#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PythonチュートリアルのMarkdownファイルをHTMLに変換するスクリプト
"""

import markdown
from pygments.formatters import HtmlFormatter
import os

def convert_markdown_to_html():
    """MarkdownファイルをHTMLに変換"""
    
    # 入力ファイルと出力ファイルのパス
    input_file = "Python_Beginner_Tutorial_Complete.md"
    output_file = "Python_Beginner_Tutorial_Complete.html"
    
    # Markdownファイルを読み込み
    print(f"'{input_file}'を読み込んでいます...")
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            markdown_content = f.read()
    except FileNotFoundError:
        print(f"エラー: '{input_file}'が見つかりません。")
        return
    
    # Markdown拡張機能の設定
    extensions = [
        'codehilite',           # シンタックスハイライト
        'toc',                  # 目次生成
        'tables',               # テーブルサポート
        'fenced_code',          # コードブロック
        'footnotes',            # 脚注
        'attr_list',            # 属性リスト
        'def_list',             # 定義リスト
        'abbr',                 # 略語
        'nl2br',                # 改行をbrタグに変換
    ]
    
    # Markdown設定
    extension_configs = {
        'codehilite': {
            'css_class': 'highlight',
            'linenums': False,
        },
        'toc': {
            'title': '目次',
            'anchorlink': True,
        }
    }
    
    # MarkdownをHTMLに変換
    print("MarkdownをHTMLに変換しています...")
    md = markdown.Markdown(
        extensions=extensions,
        extension_configs=extension_configs
    )
    html_body = md.convert(markdown_content)
    
    # Pygmentsのスタイルを取得（Flask tutorialと同じmonokaiスタイルを使用）
    formatter = HtmlFormatter(style='monokai', linenos=False, cssclass='highlight')
    css_styles = formatter.get_style_defs('.highlight')
    
    # 完全なHTMLドキュメントを生成
    html_template = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python初級チュートリアル完全版</title>
    <style>
        /* リセットCSS */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        /* ベーススタイル */
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
        
        /* 水平線 */
        hr {{
            border: none;
            height: 1px;
            background-color: #ecf0f1;
            margin: 2rem 0;
        }}
        
        /* 注意書き */
        .note {{
            background-color: #d4edda;
            border: 1px solid #c3e6cb;
            border-radius: 5px;
            padding: 15px;
            margin: 20px 0;
        }}
        
        .warning {{
            background-color: #f8d7da;
            border: 1px solid #f5c6cb;
            border-radius: 5px;
            padding: 15px;
            margin: 20px 0;
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
        
        /* シンタックスハイライト (Pygments) */
        {css_styles}
        
        /* コードブロックの追加スタイル */
        .highlight {{
            background-color: #272822;
            border-radius: 5px;
            padding: 1rem;
            overflow-x: auto;
            margin: 1rem 0;
        }}
        
        .highlight pre {{
            margin: 0;
            padding: 0;
            background-color: transparent;
            box-shadow: none;
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
        
        /* 目次へ戻るボタン */
        .back-to-top {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border-radius: 50%;
            text-decoration: none;
            box-shadow: 0 2px 5px rgba(0,0,0,0.3);
            font-size: 18px;
        }}
        
        .back-to-top:hover {{
            background-color: #e74c3c;
            color: white;
        }}
    </style>
</head>
<body>
    <div class="container">
        {html_body}
        <div class="footer">
            <p>Python初級チュートリアル完全版 - Generated with Python Markdown</p>
        </div>
    </div>
    <a href="#" class="back-to-top" title="ページトップに戻る">↑</a>
    
    <script>
        // ページトップに戻る機能
        document.querySelector('.back-to-top').addEventListener('click', function(e) {{
            e.preventDefault();
            window.scrollTo({{
                top: 0,
                behavior: 'smooth'
            }});
        }});
        
        // 目次リンクのスムーススクロール
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{
                        behavior: 'smooth',
                        block: 'start'
                    }});
                }}
            }});
        }});
        
        // コードブロックにコピー機能を追加
        document.querySelectorAll('pre').forEach(pre => {{
            const button = document.createElement('button');
            button.textContent = 'コピー';
            button.style.cssText = `
                position: absolute;
                top: 10px;
                right: 10px;
                background: #3498db;
                color: white;
                border: none;
                padding: 5px 10px;
                border-radius: 3px;
                cursor: pointer;
                font-size: 12px;
            `;
            
            pre.style.position = 'relative';
            pre.appendChild(button);
            
            button.addEventListener('click', () => {{
                const code = pre.querySelector('code') || pre;
                navigator.clipboard.writeText(code.textContent).then(() => {{
                    button.textContent = 'コピー完了!';
                    setTimeout(() => {{
                        button.textContent = 'コピー';
                    }}, 2000);
                }});
            }});
        }});
    </script>
</body>
</html>"""
    
    # HTMLファイルに書き込み
    print(f"'{output_file}'に保存しています...")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_template)
    
    print(f"変換完了! '{output_file}'が生成されました。")
    print(f"ファイルサイズ: {os.path.getsize(output_file):,} bytes")

if __name__ == "__main__":
    print("Python初級チュートリアル Markdown → HTML 変換ツール")
    print("=" * 50)
    convert_markdown_to_html()
    print("=" * 50)
    print("変換処理が完了しました。")