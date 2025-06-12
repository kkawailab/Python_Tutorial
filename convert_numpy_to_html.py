#!/usr/bin/env python3
"""
NumPyチュートリアルをHTMLに変換するスクリプト
他のチュートリアルと同じPygments構文ハイライトを使用
"""

import markdown
from pygments.formatters import HtmlFormatter

def convert_markdown_to_html(md_content):
    """MarkdownをHTMLに変換（Pygmentsスタイル付き）"""
    
    # Markdown拡張機能の設定
    extensions = [
        'codehilite',
        'fenced_code',
        'tables',
        'toc',
        'nl2br'
    ]
    
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
    md = markdown.Markdown(
        extensions=extensions,
        extension_configs=extension_configs
    )
    html_body = md.convert(md_content)
    
    # Pygmentsのスタイルを取得（monokaiスタイル）
    formatter = HtmlFormatter(style='monokai', linenos=False, cssclass='highlight')
    css_styles = formatter.get_style_defs('.highlight')
    
    # HTMLテンプレート
    html_template = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NumPy完全チュートリアル</title>
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
        
        /* コードブロック */
        pre {{
            margin: 1rem 0;
        }}
        
        .highlight {{
            background-color: #272822 !important;
            border-radius: 5px;
            overflow-x: auto;
        }}
        
        .highlight pre {{
            background-color: transparent !important;
            margin: 0;
            padding: 1rem;
            color: #F8F8F2;
        }}
        
        /* インラインコード */
        code:not(.highlight > pre > code) {{
            background-color: #f0f0f0;
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            font-family: 'Monaco', 'Consolas', 'Courier New', monospace;
            font-size: 0.9em;
            color: #e74c3c;
        }}
        
        /* Pygments構文ハイライトスタイル */
        {css_styles}
        
        /* テーブル */
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 1rem 0;
        }}
        
        th, td {{
            border: 1px solid #ddd;
            padding: 0.5rem;
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
        
        /* リンク */
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        /* 引用 */
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 1rem;
            margin: 1rem 0;
            font-style: italic;
            color: #666;
        }}
        
        /* 目次 */
        .toc {{
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 5px;
            padding: 1.5rem;
            margin: 2rem 0;
        }}
        
        .toc > ul {{
            list-style-type: none;
            padding-left: 0;
        }}
        
        .toc ul ul {{
            padding-left: 1.5rem;
        }}
        
        .toc li {{
            margin: 0.3rem 0;
        }}
        
        .toc a {{
            color: #495057;
        }}
        
        .toc a:hover {{
            color: #3498db;
        }}
        
        /* 注意・警告ボックス */
        .note {{
            background-color: #e3f2fd;
            border-left: 4px solid #2196f3;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 0 5px 5px 0;
        }}
        
        .warning {{
            background-color: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 0 5px 5px 0;
        }}
        
        /* レスポンシブデザイン */
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
            
            pre {{
                padding: 0.5rem;
                font-size: 0.85rem;
            }}
            
            table {{
                font-size: 0.9rem;
            }}
        }}
        
        /* ナビゲーション */
        .nav {{
            position: fixed;
            top: 20px;
            right: 20px;
            background-color: white;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        
        .nav a {{
            margin: 0 0.5rem;
            font-size: 0.9rem;
        }}
        
        /* スクロールトップボタン */
        .scroll-top {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #3498db;
            color: white;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            opacity: 0;
            transition: opacity 0.3s;
            text-decoration: none;
        }}
        
        .scroll-top.visible {{
            opacity: 1;
        }}
        
        .scroll-top:hover {{
            background-color: #2980b9;
            text-decoration: none;
        }}
        
        /* フッター */
        .footer {{
            margin-top: 4rem;
            padding-top: 2rem;
            border-top: 1px solid #ecf0f1;
            text-align: center;
            color: #666;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <div class="nav">
        <a href="index.html">ホーム</a>
        <a href="Python_Beginner_Tutorial_Complete.html">Python初級</a>
        <a href="Flask_Tutorial_Complete.html">Flask</a>
    </div>
    
    <div class="container">
        {html_body}
        
        <div class="footer">
            <p>NumPy完全チュートリアル - Pythonで科学計算をマスターしよう</p>
            <p>&copy; 2024 Python Tutorial. All rights reserved.</p>
        </div>
    </div>
    
    <a href="#" class="scroll-top" id="scrollTop">↑</a>
    
    <script>
        // スクロールトップボタンの表示/非表示
        window.addEventListener('scroll', function() {{
            const scrollTop = document.getElementById('scrollTop');
            if (window.pageYOffset > 200) {{
                scrollTop.classList.add('visible');
            }} else {{
                scrollTop.classList.remove('visible');
            }}
        }});
        
        // スムーズスクロール
        document.getElementById('scrollTop').addEventListener('click', function(e) {{
            e.preventDefault();
            window.scrollTo({{
                top: 0,
                behavior: 'smooth'
            }});
        }});
        
        // 目次のスムーズスクロール
        document.querySelectorAll('.toc a').forEach(anchor => {{
            anchor.addEventListener('click', function(e) {{
                e.preventDefault();
                const targetId = this.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                if (targetElement) {{
                    targetElement.scrollIntoView({{
                        behavior: 'smooth',
                        block: 'start'
                    }});
                }}
            }});
        }});
    </script>
</body>
</html>"""
    
    return html_template

def main():
    # MarkdownファイルをHTMLに変換
    try:
        with open('NumPy_Tutorial_Complete.md', 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        html_content = convert_markdown_to_html(markdown_content)
        
        with open('NumPy_Tutorial_Complete.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print("NumPy_Tutorial_Complete.html を生成しました。")
        
    except FileNotFoundError:
        print("エラー: NumPy_Tutorial_Complete.md が見つかりません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()