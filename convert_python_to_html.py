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
    
    # Pygmentsのスタイルを取得
    formatter = HtmlFormatter(style='colorful', linenos=False, cssclass='highlight')
    css_styles = formatter.get_style_defs('.highlight')
    
    # 完全なHTMLドキュメントを生成
    html_template = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python初級チュートリアル完全版</title>
    <style>
        /* ベーススタイル */
        body {{
            font-family: 'Segoe UI', 'Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif;
            line-height: 1.8;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
            background-color: #f8f9fa;
        }}
        
        /* ヘッダー */
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 30px;
            font-size: 2.5em;
        }}
        
        h2 {{
            color: #34495e;
            border-bottom: 2px solid #e74c3c;
            padding-bottom: 8px;
            margin-top: 40px;
            margin-bottom: 20px;
            font-size: 2em;
        }}
        
        h3 {{
            color: #2980b9;
            margin-top: 30px;
            margin-bottom: 15px;
            font-size: 1.5em;
        }}
        
        h4 {{
            color: #16a085;
            margin-top: 25px;
            margin-bottom: 10px;
            font-size: 1.2em;
        }}
        
        /* パラグラフ */
        p {{
            margin-bottom: 15px;
            text-align: justify;
        }}
        
        /* リスト */
        ul, ol {{
            margin-bottom: 15px;
            padding-left: 30px;
        }}
        
        li {{
            margin-bottom: 8px;
        }}
        
        /* 目次 */
        .toc {{
            background-color: #ecf0f1;
            border: 2px solid #bdc3c7;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 30px;
        }}
        
        .toc ul {{
            list-style-type: none;
            padding-left: 0;
        }}
        
        .toc li {{
            margin-bottom: 5px;
        }}
        
        .toc a {{
            color: #2980b9;
            text-decoration: none;
            font-weight: 500;
        }}
        
        .toc a:hover {{
            color: #e74c3c;
            text-decoration: underline;
        }}
        
        /* コードブロック */
        pre {{
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 8px;
            padding: 20px;
            overflow-x: auto;
            margin: 20px 0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            line-height: 1.6;
        }}
        
        code {{
            font-family: 'SF Mono', 'Monaco', 'Inconsolata', 'Roboto Mono', 'Source Code Pro', monospace;
            font-size: 0.9em;
        }}
        
        /* インラインコード */
        p code, li code, td code {{
            background-color: #f4f4f4;
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            color: #e74c3c;
            font-size: 0.85rem;
            border: 1px solid #ddd;
        }}
        
        /* テーブル */
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            background-color: white;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        
        th {{
            background-color: #3498db;
            color: white;
            font-weight: bold;
        }}
        
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        
        /* 引用 */
        blockquote {{
            border-left: 4px solid #3498db;
            margin: 20px 0;
            padding: 10px 20px;
            background-color: #ecf0f1;
            font-style: italic;
        }}
        
        /* リンク */
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        
        a:hover {{
            color: #e74c3c;
            text-decoration: underline;
        }}
        
        /* セクション区切り */
        hr {{
            border: none;
            height: 2px;
            background: linear-gradient(to right, #3498db, #e74c3c);
            margin: 40px 0;
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
        
        /* レスポンシブデザイン */
        @media (max-width: 768px) {{
            body {{
                padding: 10px;
                font-size: 14px;
            }}
            
            h1 {{
                font-size: 2em;
            }}
            
            h2 {{
                font-size: 1.5em;
            }}
            
            pre {{
                padding: 10px;
                font-size: 0.8em;
            }}
        }}
        
        /* カスタムシンタックスハイライト */
        .highlight {{
            background-color: #f8f9fa;
        }}
        
        /* コメント */
        .highlight .c, .highlight .c1, .highlight .cm {{
            color: #6c757d;
            font-style: italic;
        }}
        
        /* キーワード */
        .highlight .k, .highlight .kn, .highlight .kd, .highlight .kc {{
            color: #0066cc;
            font-weight: 600;
        }}
        
        /* 文字列 */
        .highlight .s, .highlight .s1, .highlight .s2, .highlight .sb, .highlight .sc, .highlight .sd, .highlight .se, .highlight .sh, .highlight .si, .highlight .sx {{
            color: #28a745;
        }}
        
        /* 数値 */
        .highlight .m, .highlight .mi, .highlight .mf, .highlight .mh, .highlight .mo {{
            color: #dc3545;
        }}
        
        /* 関数名 */
        .highlight .nf {{
            color: #6f42c1;
            font-weight: 500;
        }}
        
        /* クラス名 */
        .highlight .nc {{
            color: #e83e8c;
            font-weight: 600;
        }}
        
        /* 変数名 */
        .highlight .n, .highlight .nb, .highlight .nv {{
            color: #495057;
        }}
        
        /* 演算子 */
        .highlight .o, .highlight .ow {{
            color: #6c757d;
        }}
        
        /* 括弧 */
        .highlight .p {{
            color: #6c757d;
        }}
        
        /* デコレータ */
        .highlight .nd {{
            color: #fd7e14;
            font-weight: 500;
        }}
        
        /* エラー */
        .highlight .err {{
            color: #dc3545;
        }}
        
        /* self, cls */
        .highlight .bp {{
            color: #6f42c1;
            font-style: italic;
        }}
        
        /* True, False, None */
        .highlight .kc {{
            color: #e83e8c;
            font-weight: 600;
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
    {html_body}
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