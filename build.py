#!/usr/bin/env python3
"""株式会社エムアイジャパン コーポレートサイト ビルダー（単一正本）。
HTMLは直接編集しない。内容・構造の変更は必ずこのファイルへ。"""
import os
import pathlib

ROOT = pathlib.Path(__file__).parent
# プレビュー公開(GitHub Pages等)では MIJAPAN_NOINDEX=1 で検索避け。本番(mi-japan.net)は未指定で付かない
NOINDEX = '<meta name="robots" content="noindex,nofollow">\n' if os.environ.get("MIJAPAN_NOINDEX") else ""
SITE = "株式会社エムアイジャパン"
SITE_EN = "MI JAPAN Co., Ltd."
TEL = "0276-56-9068"
TEL_RAW = "0276569068"
HOURS = "平日 9:00-18:00"
MAIL = "info@mi-japan.net"
FORM_ENDPOINT = "https://formsubmit.co/info@mi-japan.net"  # ※メール開設後に有効化
LICENSE_INTRO = "有料職業紹介事業 許可番号 10-ユ-300568"
LICENSE_SUPPORT = "登録支援機関 登録番号 26登-013978"
ADDR = "〒374-0016　群馬県館林市松原1丁目9番地1　黒沢第2ビル301"

# ---- ナビ（label, href） ----
NAV = [
    ("ホーム", "index.html"),
    ("事業内容", "services.html"),
    ("導入事例", "works.html"),
    ("会社概要", "company.html"),
    ("コラム", "column/index.html"),
    ("お問い合わせ", "contact.html"),
]

# ---- お知らせ（日付, カテゴリ, 本文） ----
NEWS = [
    ("2026.10.15", "お知らせ", "出入国在留管理庁より登録支援機関（登録番号 26登-013978）として登録されました。特定技能外国人の受入れ支援を開始します。"),
    ("2026.10.01", "お知らせ", "コーポレートサイトをリニューアルいたしました。今後とも株式会社エムアイジャパンをよろしくお願いいたします。"),
    ("2026.09.01", "採用支援", "製造・建設・食品・物流分野を中心に、即戦力となる外国人材のご紹介を強化しています。お気軽にご相談ください。"),
]

# ---- 事業（slug, 名称, リード, 画像, ポイント[(見出し,説明)]） ----
SERVICES = [
    (
        "agency", "有料職業紹介事業", LICENSE_INTRO,
        "work-factory.jpg",
        "製造・建設・食品・物流をはじめ全職種に対応。永住者・定住者・日本人の配偶者等など、就労に制限のない在留資格を持つ外国人材を中心に、今すぐ働ける即戦力をご紹介します。",
        [
            ("全職種に対応", "厚生労働大臣の許可（10-ユ-300568・全職種）のもと、幅広い業種・職種でご紹介が可能です。"),
            ("即戦力・就労制限なし", "身分系の在留資格が中心のため、残業・夜勤・配置転換も日本人社員と同じようにお任せいただけます。"),
            ("独自の海外ルート", "バングラデシュ・ネパール・スリランカ・インドを中心に、求人媒体に頼らない独自ルートで母集団を確保します。"),
            ("完全成功報酬", "ご相談・ご提案・面接調整まで無料。費用が発生するのはご入社が決まった時の1回のみです。"),
        ],
    ),
    (
        "tokutei", "特定技能外国人支援・登録支援事業", LICENSE_SUPPORT,
        "work-construction.jpg",
        "登録支援機関（26登-013978）として、特定技能外国人の受入れを一気通貫でサポート。企業さまの事務負担を軽減し、外国人材が安心して長く働ける環境づくりを支援します。",
        [
            ("登録支援機関として登録", "出入国在留管理庁の登録支援機関（26登-013978）として、特定技能1号の支援計画の作成・実施を代行します。"),
            ("義務的支援を一括代行", "事前ガイダンス・出入国の送迎・住居確保・生活オリエンテーション・各種手続き同行など、受入れに必要な支援を代行します。"),
            ("多言語での定期面談", "母国語を交えた定期面談と相談対応で、就業・生活のトラブルを早期に把握し、定着を支援します。"),
            ("幅広い分野に対応", "製造・建設・食品・外食・介護・農業・宿泊など、特定技能の対象分野に幅広く対応します。"),
        ],
    ),
]

# ---- 強み（アイコンkey, 見出し, 説明） ----
STRENGTHS = [
    ("clock", "最短1週間でご紹介", "日本国内で働く意欲の高い人材が中心。ビザの待ち時間なく、ご相談から最短1週間で面接・入社が可能です。"),
    ("shield", "紹介から定着まで一気通貫", "人材紹介と特定技能の登録支援を自社で担うため、採用後の定着フォローまで一貫して対応できます。"),
    ("globe", "代表自身が外国人材", "代表はバングラデシュから来日し2015年に日本国籍を取得。働く側の不安が分かるからこそ、ミスマッチを防げます。"),
    ("yen", "初期費用0円・明朗会計", "紹介は完全成功報酬、支援は内容に応じた明朗なお見積り。初めての外国人採用でも安心して始められます。"),
]

# ---- 導入事例（業種/規模, タイトル, 課題, 提案, メトリクス[(値,ラベル)]） ----
WORKS = [
    ("製造業／従業員80名", "埼玉県・金属加工メーカー",
     "求人を出しても応募ゼロが半年続き、派遣で穴埋め。時給上昇で人件費が限界に達していた。",
     "永住者・定住者の20〜30代を4名ご紹介。夜勤シフトに入れる方を優先して選定。",
     [("4名", "採用人数"), ("10日", "相談から入社まで"), ("0円", "月額費用")]),
    ("食品製造／従業員150名", "千葉県・惣菜製造工場",
     "技能実習の受入れを検討したが、入国まで8ヶ月待ちと判明。繁忙期に間に合わなかった。",
     "日本人の配偶者等・永住者を中心に6名。日本語での指示理解に問題のない層を配置。",
     [("6名", "採用人数"), ("2週間", "相談から入社まで"), ("100%", "1年定着率")]),
    ("建設業／従業員25名", "茨城県・内装工事会社",
     "職人の平均年齢が55歳を超え、若手が定着しない。数年後に現場が回らなくなる危機感があった。",
     "体力面と長期就労意欲を重視し、20代の定住者2名をご紹介。入社後3ヶ月は月1回面談を実施。",
     [("2名", "採用人数"), ("1週間", "相談から入社まで"), ("26歳", "平均年齢")]),
]

# ---- コラム記事（slug, カテゴリ, 日付, タイトル, 概要, 画像, 本文HTML） ----
ARTICLES = [
    (
        "tokutei-vs-ginojisshu", "特定技能", "2026.10.10",
        "特定技能と技能実習は何が違う？企業目線で分かりやすく解説",
        "「外国人採用＝技能実習」と思われがちですが、目的が労働力の確保なら特定技能の方が現実的なケースが多くあります。両者の違いを企業の視点で整理します。",
        "interview.jpg",
        """
<p>外国人材の受入れを検討し始めると、まず迷うのが「技能実習」と「特定技能」のどちらを選ぶべきか、という点です。名前は似ていますが、制度の目的も、企業にとっての使い勝手も大きく異なります。本記事では、採用する企業の視点から両者の違いを整理します。</p>
<h2>そもそも目的が違う</h2>
<p>技能実習は、日本で身につけた技能を母国に持ち帰ってもらう「国際貢献・技能移転」が本来の目的です。一方の特定技能は、人手不足の分野で「即戦力として働いてもらう」ことを目的に2019年に新設された在留資格です。この目的の違いが、職種の自由度や受入れ手続きの違いにそのまま表れます。</p>
<h2>就業までのスピードと費用</h2>
<p>技能実習は入国までに半年から1年ほどかかり、監理団体への毎月の監理費が発生します。特定技能も登録支援機関への支援委託費が毎月かかりますが、すでに日本国内にいる有資格者を採用できれば、技能実習より早く就業してもらえるケースが多くあります。</p>
<h2>どちらを選ぶべきか</h2>
<p>「技能移転を通じた国際貢献」に意義を感じるなら技能実習、「とにかく現場の人手を早く確保したい」なら特定技能、というのが大まかな目安です。さらに、永住者・定住者・日本人の配偶者等といった身分系の在留資格を持つ方であれば、職種の制限も毎月の費用もなく、日本人と同じ条件で雇用できます。</p>
<p>当社は有料職業紹介事業と登録支援機関の両方を自社で担っています。「自社の場合はどの制度が合うのか」という段階からご相談いただけますので、お気軽にお問い合わせください。</p>
""",
    ),
    (
        "mibunkei-merit", "採用ノウハウ", "2026.09.20",
        "就労制限のない在留資格（永住・定住・配偶者）を採用するメリット",
        "特定技能や技能実習が注目されがちですが、「今すぐ・自由に・長く」働ける人材を探すなら、身分系の在留資格が有力な選択肢になります。",
        "work-logistics.jpg",
        """
<p>外国人採用というと特定技能や技能実習が話題になりがちですが、製造・建設・物流などの現場で「今すぐ戦力がほしい」場合、永住者・定住者・日本人の配偶者等といった<strong>身分にもとづく在留資格</strong>の方が、もっとも扱いやすい選択肢になることがあります。</p>
<h2>働き方に制限がない</h2>
<p>身分系の在留資格は、就労する職種や時間に法律上の制限がありません。そのため、残業・夜勤・交替勤務・配置転換を、日本人社員とまったく同じようにお任せできます。繁忙期のシフトにも柔軟に対応できるのは、現場にとって大きな利点です。</p>
<h2>毎月の費用がかからない</h2>
<p>技能実習の監理費や特定技能の支援委託費のような、毎月の固定費がかかりません。採用時の紹介料のみで、月々のランニングコストを抑えられます。</p>
<h2>長期就労が前提</h2>
<p>生活基盤を日本に置いている方が多いため、腰を据えて長く働いてもらいやすいのも特長です。教育した内容が社内に蓄積し、現場のノウハウが残ります。</p>
<p>当社は、こうした身分系人材を独自の海外ルートと国内ネットワークからご紹介しています。「まず1名から試したい」というご相談も歓迎しています。</p>
""",
    ),
    (
        "ukeire-flow", "採用ノウハウ", "2026.09.05",
        "はじめての外国人採用｜ご相談から入社・定着までの流れ",
        "外国人採用が初めての企業さま向けに、当社にご相談いただいてから入社・定着支援までの流れを、ステップごとに分かりやすくご説明します。",
        "work-factory.jpg",
        """
<p>「外国人を採用したいが、何から始めればいいか分からない」というご相談を多くいただきます。本記事では、当社にお問い合わせいただいてから入社・定着までの流れを、5つのステップでご説明します。</p>
<h2>ステップ1〜2：お問い合わせとヒアリング</h2>
<p>まずは電話・フォーム・LINEのいずれかからご連絡ください。業務内容・必要人数・勤務条件・時給などをお伺いし、どのような在留資格・制度が合うかをご提案します。この段階では費用は一切かかりません。</p>
<h2>ステップ3〜4：人材のご提案と面接</h2>
<p>経歴・在留資格・日本語レベルを添えて候補者をご提案します。面接は対面・オンラインどちらも可能で、必要に応じて当社が同席し、通訳や条件のすり合わせをサポートします。</p>
<h2>ステップ5：入社・定着支援</h2>
<p>雇用手続きをサポートし、入社後も本人・企業さま双方と連絡を取り続けます。特定技能の場合は登録支援機関として、生活面・就業面の支援を継続します。小さな不満が退職に発展する前に解消できる体制です。</p>
<p>初めての受入れでも、受入れ体制の整備から入社後のフォローまで伴走しますのでご安心ください。</p>
""",
    ),
]

EXT = ' target="_blank" rel="noopener"'

# Google Tag Manager（LP と統一：GTM-NKFNLKCG）。f-string に差し込む定数（内部の波括弧はそのまま）
GTM_HEAD = """<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-NKFNLKCG');</script>
<!-- End Google Tag Manager -->"""
GTM_NOSCRIPT = """<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-NKFNLKCG"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""


# ====================== 共通パーツ ======================
def rel_prefix(depth: int) -> str:
    return "../" * depth


def nav_links(active: str, depth: int) -> str:
    out = []
    pre = rel_prefix(depth)
    for label, href in NAV:
        is_active = (href == active) or (active.startswith("column/") and href.startswith("column/"))
        cls = ' class="active"' if is_active else ""
        out.append(f'<a href="{pre}{href}"{cls}>{label}</a>')
    return "".join(out)


def header(active: str, depth: int = 0) -> str:
    pre = rel_prefix(depth)
    return f"""<header id="hd">
  <div class="hd-in">
    <a class="brand" href="{pre}index.html"><img src="{pre}assets/logo.png" alt="{SITE}"></a>
    <nav class="gnav">{nav_links(active, depth)}</nav>
    <div class="hd-cta">
      <a class="hd-tel" href="tel:{TEL_RAW}"><span class="t">{TEL}</span><span class="h">{HOURS}</span></a>
      <a class="hd-btn" href="{pre}contact.html">お問い合わせ</a>
    </div>
    <button class="burger" aria-label="メニュー" onclick="document.body.classList.toggle('mopen')"><span></span><span></span><span></span></button>
  </div>
  <nav class="mnav">{nav_links(active, depth)}<a class="mnav-tel" href="tel:{TEL_RAW}">電話する {TEL}</a></nav>
</header>"""


def footer(depth: int = 0) -> str:
    pre = rel_prefix(depth)
    links = "".join(f'<a href="{pre}{href}">{label}</a>' for label, href in NAV)
    return f"""<footer>
  <div class="ft-in">
    <div class="ft-brand">
      <img src="{pre}assets/logo.png" alt="{SITE}">
      <p class="ft-addr">{ADDR}<br>TEL {TEL} ／ FAX 0276-56-9734</p>
      <p class="ft-lic"><span>{LICENSE_INTRO}</span><span>{LICENSE_SUPPORT}</span></p>
    </div>
    <nav class="ft-nav">{links}<a href="{pre}privacy.html">プライバシーポリシー</a></nav>
  </div>
  <p class="copy">© {SITE_EN} All Rights Reserved.</p>
</footer>"""


def page(path: str, title: str, desc: str, body: str, active: str, depth: int = 0) -> None:
    pre = rel_prefix(depth)
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
{NOINDEX}{GTM_HEAD}
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{pre}assets/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{pre}assets/favicon-32.png">
<link rel="apple-touch-icon" href="{pre}assets/favicon-180.png">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="format-detection" content="telephone=no">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&family=Inter:wght@600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}assets/style.css">
</head>
<body>
{GTM_NOSCRIPT}
{header(active, depth)}
<main>
{body}
</main>
{footer(depth)}
<a class="pagetop" href="#top" aria-label="ページ上部へ">↑</a>
<div class="mbar">
  <a href="tel:{TEL_RAW}" class="mb-tel">電話</a>
  <a href="{pre}contact.html" class="mb-form">お問い合わせ</a>
</div>
<script src="{pre}assets/app.js"></script>
</body>
</html>"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def crumbs(items: list, depth: int) -> str:
    pre = rel_prefix(depth)
    parts = [f'<a href="{pre}index.html">ホーム</a>']
    for i, (label, href) in enumerate(items):
        if href and i < len(items) - 1:
            parts.append(f'<a href="{pre}{href}">{label}</a>')
        else:
            parts.append(f'<span>{label}</span>')
    return '<div class="crumbs wrap">' + '<i>/</i>'.join(parts) + '</div>'


def page_hero(label: str, title: str, lead: str, img: str, depth: int) -> str:
    pre = rel_prefix(depth)
    return f"""<section class="phero" style="background-image:linear-gradient(100deg,rgba(14,10,48,.86),rgba(20,15,70,.58) 55%,rgba(23,169,219,.42)),url('{pre}assets/{img}');background-size:cover;background-position:center">
  <div class="phero-in reveal">
    <span class="eyebrow light">{label}</span>
    <h1>{title}</h1>
    <p>{lead}</p>
  </div>
</section>"""


def sec_head(label: str, title: str, sub: str = "") -> str:
    s = f'<p class="sec-sub">{sub}</p>' if sub else ""
    return f"""<div class="sec-head reveal"><span class="eyebrow">{label}</span><h2>{title}</h2>{s}</div>"""


ICON = {
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "shield": '<path d="M12 3l7 3v5c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
    "yen": '<path d="M7 5l5 7 5-7M12 12v7M8 14h8M8 17h8"/>',
}


def cta_band(depth: int) -> str:
    pre = rel_prefix(depth)
    return f"""<section class="cta-band">
  <div class="cta-in reveal">
    <h2>まずは、お気軽にご相談ください。</h2>
    <p>「制度がよく分からない」「相場を知りたい」という段階でも構いません。<br>採用のご予定が固まっていない企業さまからのご相談も歓迎しています。</p>
    <div class="cta-btns">
      <a class="btn-tel" href="tel:{TEL_RAW}"><span class="no">{TEL}</span><span class="hr">{HOURS}</span></a>
      <a class="btn-form" href="{pre}contact.html">お問い合わせフォーム</a>
    </div>
  </div>
</section>"""


# ====================== 各ページ ======================
def build_top() -> None:
    # お知らせ
    news = "".join(
        f'<a class="news-row reveal" href="column/index.html"><span class="nd">{d}</span><span class="nc">{c}</span><span class="nt">{t}</span></a>'
        for d, c, t in NEWS
    )
    # 事業カード
    svc = ""
    for slug, name, lic, img, lead, _pts in SERVICES:
        svc += f"""<a class="svc-card reveal" href="services.html#{slug}">
  <div class="svc-img" style="background-image:url('assets/{img}')"></div>
  <div class="svc-body"><span class="svc-lic">{lic}</span><h3>{name}</h3><p>{lead}</p><span class="more">詳しく見る →</span></div>
</a>"""
    # 強み
    strengths = ""
    for key, h, d in STRENGTHS:
        strengths += f"""<div class="st-card reveal"><div class="st-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICON[key]}</svg></div><h3>{h}</h3><p>{d}</p></div>"""
    # 事例
    works = ""
    for ind, ttl, _issue, _plan, metrics in WORKS:
        ms = "".join(f'<div class="m"><b>{v}</b><span>{l}</span></div>' for v, l in metrics)
        works += f"""<a class="wk-card reveal" href="works.html"><span class="wk-ind">{ind}</span><h3>{ttl}</h3><div class="wk-m">{ms}</div></a>"""

    body = f"""
<section class="hero" id="top">
  <div class="hero-deco" aria-hidden="true"></div>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <span class="hero-eyebrow reveal">人材紹介 <i>×</i> 特定技能 受入れ支援</span>
      <h1 class="reveal">人も、企業も、<br><em>元気にする</em>。</h1>
      <p class="hero-lead reveal">製造・建設・食品・物流の人材不足を、今すぐ働ける外国人材で解決。人材紹介から特定技能の受入れ支援まで、ワンストップでサポートします。</p>
      <div class="hero-cta reveal">
        <a class="btn-form" href="contact.html">無料で相談する</a>
        <a class="btn-ghost" href="services.html">事業内容を見る</a>
      </div>
      <div class="hero-badges reveal">
        <span>{LICENSE_INTRO}</span><span>{LICENSE_SUPPORT}</span>
      </div>
    </div>
    <div class="hero-visual reveal">
      <div class="hero-figure"><img src="assets/hero-main.jpg" alt="企業の採用担当者と外国人材" width="960" height="1280"></div>
      <div class="hero-float">
        <span class="hf-k">対応エリア</span>
        <b>関東・山梨・静岡・群馬</b>
      </div>
      <div class="hero-float hero-float2">
        <span class="hf-k">ご相談から定着まで</span>
        <b>ワンストップ支援</b>
      </div>
    </div>
  </div>
</section>

<section class="news-sec">
  <div class="wrap news-wrap">
    <div class="news-head"><span class="eyebrow">News</span><h2>お知らせ</h2></div>
    <div class="news-list">{news}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    {sec_head("Business", "2つの軸で、外国人採用を支えます", "「紹介して終わり」ではなく、受け入れ後の定着まで。人材紹介と登録支援の両面から伴走します。")}
    <div class="svc-grid">{svc}</div>
  </div>
</section>

<section class="sec sec-tint">
  <div class="wrap">
    {sec_head("Strength", "エムアイジャパンが選ばれる理由")}
    <div class="st-grid">{strengths}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    {sec_head("Works", "導入事例", "実際に外国人材の採用に切り替えた企業さまの事例です。")}
    <div class="wk-grid">{works}</div>
    <div class="center"><a class="btn-line" href="works.html">導入事例をもっと見る →</a></div>
  </div>
</section>

{cta_band(0)}
"""
    page("index.html",
         f"外国人材の紹介・特定技能の受入れ支援なら{SITE}",
         "製造・建設・食品・物流の人手不足を、今すぐ働ける外国人材で解決。有料職業紹介と登録支援機関による特定技能サポートをワンストップで提供。群馬・関東・静岡エリア対応。",
         body, "index.html", 0)


def build_services() -> None:
    blocks = ""
    for i, (slug, name, lic, img, lead, pts) in enumerate(SERVICES):
        rev = "svc-rev" if i % 2 else ""
        points = "".join(f'<div class="pt reveal"><h4>{h}</h4><p>{d}</p></div>' for h, d in pts)
        blocks += f"""<section class="svc-sec {rev}" id="{slug}">
  <div class="wrap svc-full">
    <div class="svc-full-img reveal" style="background-image:url('assets/{img}')"></div>
    <div class="svc-full-body">
      <span class="eyebrow">{"Service 0"+str(i+1)}</span>
      <span class="svc-lic">{lic}</span>
      <h2>{name}</h2>
      <p class="lead">{lead}</p>
      <div class="pt-grid">{points}</div>
    </div>
  </div>
</section>"""
    body = f"""
{page_hero("Business", "事業内容", "人材紹介と特定技能の受入れ支援。2つの事業で、企業さまの人手不足に応えます。", "work-construction.jpg", 0)}
{crumbs([("事業内容", "")], 0)}
{blocks}
{cta_band(0)}
"""
    page("services.html", f"事業内容｜{SITE}",
         "有料職業紹介事業（許可番号10-ユ-300568・全職種）と、登録支援機関（26登-013978）による特定技能外国人の受入れ支援。製造・建設・食品・物流など幅広い分野に対応します。",
         body, "services.html", 0)


def build_works() -> None:
    cards = ""
    for ind, ttl, issue, plan, metrics in WORKS:
        ms = "".join(f'<div class="m"><b>{v}</b><span>{l}</span></div>' for v, l in metrics)
        cards += f"""<article class="wk-full reveal">
  <div class="wk-full-head"><span class="wk-ind">{ind}</span><h2>{ttl}</h2></div>
  <div class="wk-full-body">
    <dl><dt>課題</dt><dd>{issue}</dd><dt>ご提案</dt><dd>{plan}</dd></dl>
    <div class="wk-m">{ms}</div>
  </div>
</article>"""
    body = f"""
{page_hero("Works", "導入事例", "派遣依存や採用難から、外国人材の直接採用に切り替えた企業さまの事例をご紹介します。", "work-logistics.jpg", 0)}
{crumbs([("導入事例", "")], 0)}
<section class="sec"><div class="wrap">
  <div class="wk-list">{cards}</div>
  <p class="note center">※ 事例は個人・企業が特定されないよう一部変更しています。成果を保証するものではありません。</p>
</div></section>
{cta_band(0)}
"""
    page("works.html", f"導入事例｜{SITE}",
         "製造・食品・建設など、外国人材の採用に切り替えた企業さまの導入事例。採用人数・入社までの期間・定着率などの実績をご紹介します。",
         body, "works.html", 0)


def build_company() -> None:
    rows = [
        ("会社名", f"{SITE}（{SITE_EN}）"),
        ("代表取締役", "イスラム モニルル"),
        ("設立", "2021年1月"),
        ("資本金", "700万円"),
        ("所在地", ADDR),
        ("電話 / FAX", f"TEL {TEL} ／ FAX 0276-56-9734"),
        ("事業内容", "有料職業紹介事業／特定技能外国人支援・登録支援事業"),
        ("許認可", f"{LICENSE_INTRO}（全職種・国内）<br>{LICENSE_SUPPORT}"),
        ("インボイス登録番号", "T5060001033369"),
        ("主要取引銀行", "群馬銀行 館林支店"),
        ("対応エリア", "群馬・東京・千葉・埼玉・神奈川・茨城・山梨・静岡"),
    ]
    table = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rows)
    body = f"""
{page_hero("Company", "会社概要", "外国人であったからこそ分かる、日本で働く喜びを。エムアイジャパンの歩みと理念。", "interview.jpg", 0)}
{crumbs([("会社概要", "")], 0)}

<section class="sec"><div class="wrap-narrow">
  {sec_head("Message", "代表者メッセージ")}
  <div class="msg reveal">
    <img class="msg-photo" src="assets/ceo.jpg" alt="代表取締役 イスラム モニルル">
    <div class="msg-body">
      <h3>「誰にも負けない努力を惜しまない」</h3>
      <p>私は日本にあこがれ、バングラデシュから来日しました。2015年に日本国籍を取得し、当社を立ち上げました。外国人であったからこそ分かる、日本で働く素晴らしさや喜びを、有能な人材に伝えられると考えています。</p>
      <p>私たちのミッションは「優秀な外国人労働者を日本の職場にマッチングさせ、業務の潤滑油として機能させていく」こと。人手が足りずに事業が止まってしまう——そんなことがないよう、企業さまと働く人の双方に誠実に向き合ってまいります。</p>
      <p class="sign">{SITE}　代表取締役　イスラム モニルル</p>
    </div>
  </div>
</div></section>

<section class="sec sec-tint"><div class="wrap-narrow">
  {sec_head("Overview", "会社情報")}
  <table class="co-table reveal">{table}</table>
</div></section>
{cta_band(0)}
"""
    page("company.html", f"会社概要｜{SITE}",
         "株式会社エムアイジャパンの会社概要。設立2021年1月、群馬県館林市。有料職業紹介事業（10-ユ-300568）および登録支援機関（26登-013978）として外国人材の紹介・支援を行っています。",
         body, "company.html", 0)


def build_column() -> None:
    # 一覧（column/index.html, depth=1）
    cards = ""
    for slug, cat, date, title, excerpt, img, _body in ARTICLES:
        cards += f"""<a class="col-card reveal" href="{slug}.html">
  <div class="col-img" style="background-image:url('../assets/{img}')"><span class="col-cat">{cat}</span></div>
  <div class="col-body"><time>{date}</time><h3>{title}</h3><p>{excerpt}</p></div>
</a>"""
    body = f"""
{page_hero("Column", "コラム", "外国人採用・特定技能・在留資格について、企業さまに役立つ情報を発信します。", "mv.jpg", 1)}
{crumbs([("コラム", "")], 1)}
<section class="sec"><div class="wrap">
  <div class="col-grid">{cards}</div>
</div></section>
{cta_band(1)}
"""
    page("column/index.html", f"コラム｜{SITE}",
         "外国人採用・特定技能・在留資格に関する企業さま向けコラム。採用ノウハウや制度解説を分かりやすくお届けします。",
         body, "column/index.html", 1)

    # 各記事（depth=1）
    for idx, (slug, cat, date, title, excerpt, img, art_body) in enumerate(ARTICLES):
        related = [a for a in ARTICLES if a[0] != slug][:2]
        rel_html = "".join(
            f'<a class="rel-card" href="{r[0]}.html"><div class="rel-img" style="background-image:url(\'../assets/{r[5]}\')"></div><div class="rel-b"><time>{r[2]}</time><h4>{r[3]}</h4></div></a>'
            for r in related
        )
        body = f"""
<article class="art">
  <div class="art-hero" style="background-image:url('../assets/{img}')"><div class="art-hero-ov"></div>
    <div class="art-hero-in"><span class="col-cat">{cat}</span><h1>{title}</h1><time>{date}</time></div>
  </div>
  {crumbs([("コラム", "column/index.html"), (title, "")], 1)}
  <div class="art-body wrap-narrow reveal">
    {art_body}
  </div>
  <div class="wrap-narrow">
    <div class="art-cta">
      <h3>外国人採用のご相談はエムアイジャパンへ</h3>
      <p>人材紹介から特定技能の受入れ支援まで、ワンストップで対応します。</p>
      <a class="btn-form" href="../contact.html">無料で相談する</a>
    </div>
    <div class="rel-wrap"><h3 class="rel-title">関連記事</h3><div class="rel-grid">{rel_html}</div></div>
  </div>
</article>
"""
        page(f"column/{slug}.html", f"{title}｜コラム｜{SITE}",
             excerpt[:110], body, "column/index.html", 1)


def build_contact() -> None:
    body = f"""
{page_hero("Contact", "お問い合わせ", "採用のご相談・制度のご質問など、お気軽にお問い合わせください。しつこい営業は一切いたしません。", "work-factory.jpg", 0)}
{crumbs([("お問い合わせ", "")], 0)}
<section class="sec"><div class="wrap-narrow">
  <div class="ct-lead reveal">
    <div class="ct-tel">
      <span class="l">お電話でのお問い合わせ</span>
      <a href="tel:{TEL_RAW}">{TEL}</a>
      <span class="h">{HOURS}</span>
    </div>
  </div>
  <form class="ct-form reveal" action="{FORM_ENDPOINT}" method="POST">
    <input type="hidden" name="_subject" value="【HP】お問い合わせ">
    <input type="hidden" name="_next" value="https://mi-japan.net/thanks.html">
    <input type="hidden" name="_template" value="table">
    <input type="text" name="_honey" style="display:none">
    <div class="fld"><label>貴社名<span class="req">必須</span></label><input type="text" name="会社名" required></div>
    <div class="fld2">
      <div class="fld"><label>ご担当者名<span class="req">必須</span></label><input type="text" name="お名前" required></div>
      <div class="fld"><label>電話番号<span class="req">必須</span></label><input type="tel" name="電話番号" required></div>
    </div>
    <div class="fld"><label>メールアドレス<span class="req">必須</span></label><input type="email" name="email" required></div>
    <div class="fld2">
      <div class="fld"><label>ご相談の種類<span class="opt">任意</span></label>
        <select name="ご相談の種類"><option value="">選択してください</option><option>人材紹介について</option><option>特定技能・登録支援について</option><option>その他</option></select></div>
      <div class="fld"><label>採用予定人数<span class="opt">任意</span></label>
        <select name="採用予定人数"><option value="">選択してください</option><option>1名</option><option>2〜3名</option><option>4〜9名</option><option>10名以上</option><option>未定・相談したい</option></select></div>
    </div>
    <div class="fld"><label>お問い合わせ内容<span class="opt">任意</span></label><textarea name="お問い合わせ内容" rows="5" placeholder="例）夜勤に入れる方を3名探しています。制度のことがよく分からないので、まず話を聞きたいです。"></textarea></div>
    <p class="privacy"><a href="privacy.html">プライバシーポリシー</a>に同意のうえ、送信してください。</p>
    <button type="submit" class="ct-submit">この内容で送信する</button>
    <p class="form-note">しつこい営業は一切いたしません。ご相談だけでも歓迎しております。</p>
  </form>
</div></section>
"""
    page("contact.html", f"お問い合わせ｜{SITE}",
         "外国人材の紹介・特定技能の受入れ支援に関するお問い合わせはこちら。電話・フォームで受け付けています。ご相談だけでも歓迎いたします。",
         body, "contact.html", 0)


def build_thanks() -> None:
    body = f"""
<section class="thanks"><div class="wrap-narrow reveal">
  <div class="th-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 12l3 3 5-6"/></svg></div>
  <h1>送信が完了しました</h1>
  <p>お問い合わせいただき、ありがとうございます。<br>担当者より、通常1〜2営業日以内にご連絡いたします。</p>
  <a class="btn-line" href="index.html">トップページへ戻る</a>
</div></section>
"""
    page("thanks.html", f"送信完了｜{SITE}", "お問い合わせの送信が完了しました。", body, "", 0)


def build_privacy() -> None:
    body = f"""
{page_hero("Privacy", "プライバシーポリシー", "", "interview.jpg", 0)}
{crumbs([("プライバシーポリシー", "")], 0)}
<section class="sec"><div class="wrap-narrow reveal art-body">
  <p>{SITE}（以下「当社」）は、人材紹介事業および登録支援業務を行うにあたり、お客様および求職者の個人情報を適切に保護することを社会的責務と考え、以下の方針に基づき個人情報を取り扱います。</p>
  <h2>1. 個人情報の取得・利用</h2>
  <p>当社は、事業の遂行に必要な範囲で個人情報を取得し、求人・求職のマッチング、支援業務の提供、ご連絡、その他これらに付随する目的のために利用します。取得にあたっては利用目的を明確にし、目的の範囲を超えた利用は行いません。</p>
  <h2>2. 法令・規範の遵守</h2>
  <p>当社は、個人情報に関する法令・国が定める指針、その他の規範を遵守し、安全に個人情報の保護を行います。</p>
  <h2>3. 適切な管理と安全対策</h2>
  <p>当社は、取り扱う個人情報について、不正アクセス・紛失・破壊・改ざん・漏えい等を防止するため、必要かつ適切な安全管理措置を講じ、継続的に見直し・改善を行います。</p>
  <h2>4. 第三者提供</h2>
  <p>当社は、法令に定める場合を除き、あらかじめご本人の同意を得ることなく個人情報を第三者に提供しません。</p>
  <h2>5. お問い合わせ</h2>
  <p>個人情報の取り扱いに関するお問い合わせは、下記までご連絡ください。<br>{SITE}　TEL {TEL}　Email {MAIL}</p>
</div></section>
"""
    page("privacy.html", f"プライバシーポリシー｜{SITE}",
         f"{SITE}のプライバシーポリシー。個人情報の取得・利用・管理に関する方針を定めています。",
         body, "", 0)


CSS = r""":root{
  --navy:#1d1653; --navy2:#2a2170; --cyan:#3dc7f4; --cyan-d:#17a9db;
  --ink:#1c2230; --mute:#6b7384; --line:#e6e9f0; --bg:#fff; --tint:#f3f7fc;
  --shadow:0 18px 44px -20px rgba(29,22,83,.26); --shadow-sm:0 8px 22px -12px rgba(29,22,83,.2);
  --radius:16px; --font:"Noto Sans JP","Hiragino Kaku Gothic ProN",system-ui,sans-serif; --num:"Inter",var(--font);
}
*{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}
html{scroll-behavior:smooth;scroll-padding-top:76px}
body{font-family:var(--font);color:var(--ink);background:var(--bg);line-height:1.9;font-size:15px}
img,svg{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
main{overflow:hidden}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
.wrap-narrow{max-width:800px;margin:0 auto;padding:0 20px}
.center{text-align:center}
.eyebrow{display:inline-block;font:800 11.5px/1 var(--num);letter-spacing:.26em;color:var(--cyan-d);text-transform:uppercase;margin-bottom:12px}
.eyebrow.light{color:#9fe3fb}
h2{font-weight:900;font-size:clamp(22px,3.6vw,33px);line-height:1.45;color:var(--navy);letter-spacing:.01em}
.note{font-size:11.5px;color:var(--mute)}

/* reveal animation */
.reveal{opacity:0;transform:translateY(26px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.7,.2,1)}
.reveal.vis{opacity:1;transform:none}

/* header */
#hd{position:fixed;top:0;left:0;right:0;z-index:100;transition:.3s;background:rgba(255,255,255,.9);backdrop-filter:blur(12px);border-bottom:1px solid rgba(230,233,240,.7)}
#hd.solid{background:rgba(255,255,255,.97);box-shadow:0 2px 20px -12px rgba(29,22,83,.4);border-bottom-color:transparent}
.hd-in{max-width:1200px;margin:0 auto;display:flex;align-items:center;gap:18px;padding:12px 20px}
.brand img{height:40px;width:auto}
.gnav{display:flex;gap:4px;margin-left:auto}
.gnav a{padding:8px 13px;font-size:14px;font-weight:700;border-radius:8px;transition:.2s;color:var(--navy)}
.gnav a:hover,.gnav a.active{color:var(--cyan-d)}
.hd-cta{display:flex;align-items:center;gap:12px}
.hd-tel{display:flex;flex-direction:column;line-height:1.2;text-align:right;color:var(--navy)}
.hd-tel .t{font:800 18px/1 var(--num)}
.hd-tel .h{font-size:10px;opacity:.85}
.hd-btn{background:linear-gradient(135deg,var(--cyan),var(--cyan-d));color:#fff;font-weight:700;font-size:13.5px;padding:10px 18px;border-radius:999px;box-shadow:var(--shadow-sm);white-space:nowrap;transition:.2s}
.hd-btn:hover{transform:translateY(-2px)}
.burger{display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:6px}
.burger span{width:24px;height:2px;background:var(--navy);transition:.3s}
.mnav{display:none}

@media(max-width:900px){
  .gnav,.hd-cta{display:none}
  .burger{display:flex;margin-left:auto}
  .mnav{position:fixed;top:0;right:0;width:76%;max-width:320px;height:100vh;background:var(--navy);flex-direction:column;padding:88px 26px 26px;gap:4px;transform:translateX(100%);transition:.35s;display:flex;z-index:99}
  body.mopen .mnav{transform:none}
  body.mopen::after{content:"";position:fixed;inset:0;background:rgba(0,0,0,.4);z-index:98}
  .mnav a{color:#fff;padding:14px 10px;font-weight:700;border-bottom:1px solid rgba(255,255,255,.12)}
  .mnav a.active{color:var(--cyan)}
  .mnav-tel{margin-top:16px;background:var(--cyan);border-radius:10px;text-align:center;border:none!important}
}

/* hero (corporate split) */
.hero{position:relative;background:linear-gradient(170deg,#f6fbff 0%,#eaf2fb 62%,#e3edf8 100%);overflow:hidden}
.hero-deco{position:absolute;top:-160px;right:-140px;width:560px;height:560px;z-index:0;background:radial-gradient(circle,rgba(61,199,244,.2),transparent 68%);pointer-events:none}
.hero-deco::after{content:"";position:absolute;left:-360px;top:360px;width:420px;height:420px;border-radius:50%;background:radial-gradient(circle,rgba(29,22,83,.07),transparent 70%)}
.hero-grid{position:relative;z-index:2;display:grid;grid-template-columns:1.04fr .96fr;gap:54px;align-items:center;padding-top:152px;padding-bottom:94px}
.hero-copy{min-width:0}
.hero-eyebrow{display:inline-flex;align-items:center;gap:8px;font:800 12px/1 var(--num);letter-spacing:.12em;color:var(--cyan-d);background:#fff;border:1px solid var(--line);padding:9px 16px;border-radius:999px;box-shadow:var(--shadow-sm);margin-bottom:26px}
.hero-eyebrow i{font-style:normal;color:var(--cyan);font-size:14px}
.hero h1{font-weight:900;font-size:clamp(37px,5.4vw,64px);line-height:1.17;letter-spacing:.012em;color:var(--navy);margin-bottom:22px}
.hero h1 em{font-style:normal;color:var(--cyan-d);position:relative;white-space:nowrap}
.hero h1 em::after{content:"";position:absolute;left:0;right:0;bottom:.06em;height:.16em;background:var(--cyan);opacity:.32;border-radius:4px;z-index:-1}
.hero-lead{font-size:clamp(14.5px,1.4vw,16.5px);color:var(--ink);opacity:.9;max-width:540px;margin-bottom:32px;line-height:1.95}
.hero-cta{display:flex;gap:14px;flex-wrap:wrap;margin-bottom:30px}
.hero-badges{display:flex;gap:9px;flex-wrap:wrap}
.hero-badges span{font-size:11.5px;font-weight:700;color:var(--navy);background:#fff;border:1px solid var(--line);padding:8px 15px;border-radius:999px;box-shadow:var(--shadow-sm)}
.hero-visual{position:relative;align-self:stretch}
.hero-figure{position:relative;border-radius:26px;overflow:hidden;aspect-ratio:4/5;box-shadow:0 44px 90px -34px rgba(29,22,83,.52);background:var(--tint)}
.hero-figure img{width:100%;height:100%;object-fit:cover;object-position:center 22%}
.hero-figure::after{content:"";position:absolute;inset:0;border-radius:26px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.35)}
.hero-float{position:absolute;background:rgba(255,255,255,.96);backdrop-filter:blur(6px);border-radius:14px;padding:12px 18px;box-shadow:var(--shadow);display:flex;flex-direction:column;line-height:1.35;animation:floaty 5s ease-in-out infinite}
.hero-float .hf-k{font-size:10.5px;color:var(--mute);font-weight:700;letter-spacing:.02em}
.hero-float b{font-size:14.5px;color:var(--navy);font-weight:900}
.hero-float{left:-22px;bottom:34px}
.hero-float2{left:auto;right:-16px;top:40px;bottom:auto;animation-delay:1.4s}
@keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}
@keyframes fadeup{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
.btn-form{display:inline-flex;align-items:center;justify-content:center;background:linear-gradient(135deg,var(--cyan),var(--cyan-d));color:#fff;font-weight:800;font-size:16px;padding:16px 34px;border-radius:999px;box-shadow:0 14px 34px -10px rgba(23,169,219,.7);transition:.2s}
.btn-form:hover{transform:translateY(-2px)}
.btn-ghost{display:inline-flex;align-items:center;justify-content:center;border:2px solid var(--navy);color:var(--navy);font-weight:700;font-size:15px;padding:14px 30px;border-radius:999px;transition:.2s;background:transparent}
.btn-ghost:hover{background:var(--navy);color:#fff;border-color:var(--navy)}
@media(max-width:900px){
  .hero-grid{grid-template-columns:1fr;gap:38px;padding-top:116px;padding-bottom:62px}
  .hero-figure{aspect-ratio:3/2;max-height:420px}
  .hero-figure img{object-position:center 26%}
  .hero-float{left:12px;bottom:14px}
  .hero-float2{right:12px;top:14px}
}

/* news */
.news-sec{background:var(--navy);color:#fff;position:relative;z-index:3}
.news-wrap{display:grid;grid-template-columns:200px 1fr;gap:20px;padding-top:34px;padding-bottom:34px}
.news-head .eyebrow{color:var(--cyan)}
.news-head h2{color:#fff}
.news-list{display:flex;flex-direction:column}
.news-row{display:flex;align-items:center;gap:16px;padding:14px 4px;border-bottom:1px solid rgba(255,255,255,.14);transition:.2s;flex-wrap:wrap}
.news-row:hover{color:var(--cyan)}
.news-row .nd{font:700 13px/1 var(--num);color:#9fe3fb;min-width:86px}
.news-row .nc{font-size:11px;font-weight:700;background:rgba(61,199,244,.2);color:#9fe3fb;padding:3px 10px;border-radius:999px}
.news-row .nt{font-size:13.5px;flex:1;min-width:200px}
@media(max-width:700px){.news-wrap{grid-template-columns:1fr;gap:10px}}

/* sections */
.sec{padding:84px 0}
.sec-tint{background:var(--tint)}
.sec-head{text-align:center;margin-bottom:46px}
.sec-sub{color:var(--mute);max-width:640px;margin:14px auto 0;font-size:14.5px}

/* service cards (top) */
.svc-grid{display:grid;grid-template-columns:1fr 1fr;gap:24px}
@media(max-width:760px){.svc-grid{grid-template-columns:1fr}}
.svc-card{background:#fff;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow-sm);transition:.28s;display:flex;flex-direction:column}
.svc-card:hover{transform:translateY(-6px);box-shadow:var(--shadow)}
.svc-img{height:210px;background-size:cover;background-position:center;transition:.4s}
.svc-card:hover .svc-img{transform:scale(1.06)}
.svc-body{padding:26px 24px 28px}
.svc-lic{display:inline-block;font:700 11px/1 var(--num);color:var(--cyan-d);background:var(--tint);padding:5px 12px;border-radius:999px;margin-bottom:12px;letter-spacing:.04em}
.svc-body h3{font-size:21px;font-weight:900;color:var(--navy);margin-bottom:10px}
.svc-body p{font-size:14px;color:var(--ink);opacity:.9}
.svc-body .more{display:inline-block;margin-top:14px;color:var(--cyan-d);font-weight:800;font-size:14px}

/* strengths */
.st-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
@media(max-width:900px){.st-grid{grid-template-columns:1fr 1fr}}
@media(max-width:520px){.st-grid{grid-template-columns:1fr}}
.st-card{background:#fff;border-radius:var(--radius);padding:30px 22px;text-align:center;box-shadow:var(--shadow-sm);transition:.25s}
.st-card:hover{transform:translateY(-5px);box-shadow:var(--shadow)}
.st-ico{width:62px;height:62px;margin:0 auto 16px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,var(--navy),var(--navy2));color:var(--cyan)}
.st-ico svg{width:30px;height:30px}
.st-card h3{font-size:16.5px;font-weight:900;color:var(--navy);margin-bottom:9px}
.st-card p{font-size:13px;color:var(--mute);line-height:1.8}

/* works */
.wk-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
@media(max-width:860px){.wk-grid{grid-template-columns:1fr;max-width:560px;margin:0 auto}}
.wk-card{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:24px 22px;box-shadow:var(--shadow-sm);transition:.25s;display:block}
.wk-card:hover{transform:translateY(-5px);box-shadow:var(--shadow)}
.wk-ind{font-size:11.5px;font-weight:700;color:var(--cyan-d)}
.wk-card h3{font-size:17px;font-weight:900;color:var(--navy);margin:6px 0 16px}
.wk-m{display:flex;gap:12px;justify-content:space-between;border-top:1px solid var(--line);padding-top:14px}
.wk-m .m{text-align:center;flex:1}
.wk-m .m b{display:block;font:900 22px/1.1 var(--num);color:var(--cyan-d)}
.wk-m .m span{font-size:10.5px;color:var(--mute)}
.btn-line{display:inline-block;margin-top:36px;color:var(--navy);font-weight:800;border:2px solid var(--navy);padding:12px 30px;border-radius:999px;transition:.2s}
.btn-line:hover{background:var(--navy);color:#fff}

/* page hero */
.phero{position:relative;min-height:340px;display:flex;align-items:center;color:#fff;background:var(--navy)}
.phero-in{position:relative;z-index:2;max-width:1080px;margin:0 auto;padding:120px 20px 56px;width:100%}
.phero h1{font-weight:900;font-size:clamp(28px,5vw,46px);margin-bottom:12px}
.phero p{max-width:620px;opacity:.95;font-size:15px}

/* crumbs */
.crumbs{display:flex;gap:8px;align-items:center;font-size:12px;color:var(--mute);padding:16px 20px;flex-wrap:wrap}
.crumbs a:hover{color:var(--cyan-d)}
.crumbs i{font-style:normal;opacity:.5}
.crumbs span{color:var(--ink)}

/* service full */
.svc-sec{padding:70px 0}
.svc-full{display:grid;grid-template-columns:.92fr 1.08fr;gap:44px;align-items:center}
.svc-sec.svc-rev .svc-full{direction:rtl}
.svc-sec.svc-rev .svc-full>*{direction:ltr}
@media(max-width:820px){.svc-full{grid-template-columns:1fr;gap:24px}}
.svc-full-img{aspect-ratio:4/3;border-radius:20px;background-size:cover;background-position:center;box-shadow:var(--shadow)}
.svc-full-body .svc-lic{margin:0 0 10px}
.svc-full-body h2{margin-bottom:14px}
.svc-full-body .lead{color:var(--ink);opacity:.92;margin-bottom:24px;font-size:15px}
.pt-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:520px){.pt-grid{grid-template-columns:1fr}}
.pt{background:var(--tint);border-radius:12px;padding:18px 18px}
.pt h4{font-size:14.5px;font-weight:900;color:var(--navy);margin-bottom:6px;padding-left:14px;position:relative}
.pt h4::before{content:"";position:absolute;left:0;top:7px;width:6px;height:6px;border-radius:50%;background:var(--cyan)}
.pt p{font-size:12.5px;color:var(--mute);line-height:1.8}

/* works full */
.wk-list{display:flex;flex-direction:column;gap:20px;max-width:860px;margin:0 auto}
.wk-full{background:#fff;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow-sm)}
.wk-full-head{background:linear-gradient(135deg,var(--navy),var(--navy2));color:#fff;padding:20px 26px}
.wk-full-head .wk-ind{color:#9fe3fb}
.wk-full-head h2{color:#fff;font-size:20px;margin-top:4px}
.wk-full-body{padding:24px 26px;display:grid;grid-template-columns:1fr 240px;gap:24px;align-items:center}
@media(max-width:680px){.wk-full-body{grid-template-columns:1fr}}
.wk-full-body dl{font-size:13.5px}
.wk-full-body dt{font-weight:800;color:var(--cyan-d);font-size:11.5px;margin-top:10px}
.wk-full-body dt:first-child{margin-top:0}
.wk-full-body dd{color:var(--ink);opacity:.9}
.wk-full-body .wk-m{border-top:none;border-left:1px solid var(--line);padding:0 0 0 20px}
@media(max-width:680px){.wk-full-body .wk-m{border-left:none;border-top:1px solid var(--line);padding:14px 0 0}}

/* company */
.msg{display:grid;grid-template-columns:200px 1fr;gap:34px;align-items:start}
@media(max-width:680px){.msg{grid-template-columns:1fr;gap:20px}}
.msg-photo{width:100%;max-width:200px;border-radius:16px;box-shadow:var(--shadow);aspect-ratio:1;object-fit:cover}
.msg-body h3{font-size:19px;font-weight:900;color:var(--navy);margin-bottom:14px}
.msg-body p{font-size:14px;margin-bottom:12px;opacity:.92}
.msg-body .sign{font-weight:700;color:var(--navy);opacity:1}
.co-table{width:100%;border-collapse:collapse;font-size:14px;background:#fff;border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow-sm)}
.co-table th,.co-table td{padding:16px 18px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
.co-table th{background:var(--navy);color:#fff;font-weight:700;width:190px;white-space:nowrap}
@media(max-width:560px){.co-table th,.co-table td{display:block;width:100%}.co-table th{width:100%}}

/* column list */
.col-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
@media(max-width:860px){.col-grid{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.col-grid{grid-template-columns:1fr}}
.col-card{background:#fff;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow-sm);transition:.25s}
.col-card:hover{transform:translateY(-5px);box-shadow:var(--shadow)}
.col-img{height:180px;background-size:cover;background-position:center;position:relative}
.col-cat{position:absolute;top:12px;left:12px;background:var(--cyan-d);color:#fff;font-size:11px;font-weight:700;padding:4px 12px;border-radius:999px}
.col-body{padding:20px}
.col-body time{font:700 12px/1 var(--num);color:var(--mute)}
.col-body h3{font-size:16px;font-weight:900;color:var(--navy);margin:8px 0 10px;line-height:1.5}
.col-body p{font-size:13px;color:var(--mute);line-height:1.8}

/* article */
.art-hero{position:relative;min-height:320px;display:flex;align-items:flex-end;background-size:cover;background-position:center;color:#fff}
.art-hero-ov{position:absolute;inset:0;background:linear-gradient(to top,rgba(14,10,48,.9),rgba(14,10,48,.2))}
.art-hero-in{position:relative;z-index:2;max-width:800px;margin:0 auto;padding:40px 20px;width:100%}
.art-hero-in h1{font-size:clamp(22px,4vw,34px);font-weight:900;margin:12px 0 8px;line-height:1.4}
.art-hero-in time{font:700 13px/1 var(--num);opacity:.9}
.art-body{padding:48px 20px}
.art-body h2{font-size:21px;margin:34px 0 14px;padding-left:16px;border-left:5px solid var(--cyan);color:var(--navy)}
.art-body p{margin-bottom:18px;font-size:15px}
.art-body strong{color:var(--navy)}
.art-cta{background:linear-gradient(135deg,var(--navy),var(--navy2));color:#fff;border-radius:20px;padding:40px 30px;text-align:center;margin:20px 0 40px}
.art-cta h3{font-size:20px;font-weight:900;margin-bottom:10px}
.art-cta p{opacity:.9;margin-bottom:22px;font-size:14px}
.rel-wrap{margin-bottom:60px}
.rel-title{font-size:18px;color:var(--navy);margin-bottom:18px;text-align:center}
.rel-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:560px){.rel-grid{grid-template-columns:1fr}}
.rel-card{display:flex;gap:14px;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;box-shadow:var(--shadow-sm);transition:.2s}
.rel-card:hover{transform:translateY(-3px);box-shadow:var(--shadow)}
.rel-img{width:96px;flex:none;background-size:cover;background-position:center}
.rel-b{padding:12px 14px}
.rel-b time{font:700 11px/1 var(--num);color:var(--mute)}
.rel-b h4{font-size:13.5px;color:var(--navy);margin-top:6px;line-height:1.5}

/* cta band */
.cta-band{background:linear-gradient(120deg,var(--navy) 0%,var(--navy2) 60%,var(--cyan-d) 160%);color:#fff;padding:72px 20px;text-align:center;position:relative;overflow:hidden}
.cta-band::after{content:"";position:absolute;top:-80px;right:-60px;width:320px;height:320px;border-radius:50%;background:radial-gradient(circle,rgba(61,199,244,.3),transparent 70%)}
.cta-in{position:relative;z-index:2;max-width:720px;margin:0 auto}
.cta-band h2{color:#fff;margin-bottom:14px}
.cta-in p{opacity:.92;margin-bottom:30px;font-size:14.5px}
.cta-btns{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.btn-tel{display:flex;flex-direction:column;background:#fff;color:var(--navy);padding:12px 28px;border-radius:999px;font-weight:800}
.btn-tel .no{font:900 22px/1.1 var(--num)}
.btn-tel .hr{font-size:10.5px;color:var(--mute)}

/* contact */
.ct-lead{text-align:center;margin-bottom:30px}
.ct-tel{display:inline-flex;flex-direction:column;gap:2px}
.ct-tel .l{font-size:12px;color:var(--mute);font-weight:700}
.ct-tel a{font:900 34px/1 var(--num);color:var(--navy)}
.ct-tel .h{font-size:12px;color:var(--mute)}
.ct-form{background:#fff;border:1px solid var(--line);border-radius:20px;padding:34px 30px;box-shadow:var(--shadow-sm)}
@media(max-width:560px){.ct-form{padding:24px 18px}}
.fld{margin-bottom:16px}
.fld label{display:block;font-size:13px;font-weight:700;color:var(--navy);margin-bottom:6px}
.req{background:#d94141;color:#fff;font-size:10px;padding:2px 7px;border-radius:4px;margin-left:7px}
.opt{background:var(--mute);color:#fff;font-size:10px;padding:2px 7px;border-radius:4px;margin-left:7px}
.fld input,.fld select,.fld textarea{width:100%;border:1.5px solid var(--line);border-radius:10px;padding:12px 14px;font-size:15px;font-family:var(--font);background:var(--tint);transition:.2s}
.fld input:focus,.fld select:focus,.fld textarea:focus{outline:none;border-color:var(--cyan);background:#fff;box-shadow:0 0 0 3px rgba(61,199,244,.16)}
.fld2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:560px){.fld2{grid-template-columns:1fr}}
.privacy{font-size:12px;color:var(--mute);text-align:center;margin:18px 0 14px}
.privacy a{color:var(--cyan-d);text-decoration:underline}
.ct-submit{width:100%;border:none;cursor:pointer;background:linear-gradient(135deg,var(--cyan),var(--cyan-d));color:#fff;font-size:17px;font-weight:900;font-family:var(--font);padding:17px;border-radius:999px;box-shadow:0 14px 30px -10px rgba(23,169,219,.6);transition:.2s}
.ct-submit:hover{transform:translateY(-2px)}
.form-note{text-align:center;font-size:11.5px;color:var(--mute);margin-top:12px}

/* thanks */
.thanks{padding:140px 20px 100px;text-align:center}
.th-ico{width:76px;height:76px;margin:0 auto 24px;border-radius:50%;background:linear-gradient(135deg,var(--cyan),var(--cyan-d));color:#fff;display:flex;align-items:center;justify-content:center}
.th-ico svg{width:40px;height:40px}
.thanks h1{font-size:28px;color:var(--navy);margin-bottom:14px}
.thanks p{color:var(--mute);margin-bottom:30px}

/* footer */
footer{background:#0e0a30;color:rgba(255,255,255,.7);padding:56px 20px 30px}
.ft-in{max-width:1080px;margin:0 auto;display:grid;grid-template-columns:1.4fr 1fr;gap:40px}
@media(max-width:720px){.ft-in{grid-template-columns:1fr;gap:26px}}
.ft-brand img{height:40px;filter:brightness(0) invert(1);margin-bottom:16px}
.ft-addr{font-size:13px;line-height:1.9}
.ft-lic{margin-top:12px;display:flex;flex-direction:column;gap:3px}
.ft-lic span{font-size:11.5px;color:#9fe3fb}
.ft-nav{display:flex;flex-direction:column;gap:10px}
.ft-nav a{font-size:13.5px;transition:.2s}
.ft-nav a:hover{color:var(--cyan)}
.copy{text-align:center;font-size:11px;color:rgba(255,255,255,.4);margin-top:40px;border-top:1px solid rgba(255,255,255,.1);padding-top:20px}

/* pagetop + mobile bar */
.pagetop{position:fixed;right:18px;bottom:84px;z-index:80;width:44px;height:44px;border-radius:50%;background:var(--navy);color:#fff;display:flex;align-items:center;justify-content:center;font-size:18px;opacity:0;pointer-events:none;transition:.3s;box-shadow:var(--shadow)}
.pagetop.show{opacity:1;pointer-events:auto}
@media(min-width:901px){.pagetop{bottom:24px}}
.mbar{position:fixed;left:0;right:0;bottom:0;z-index:90;display:none;grid-template-columns:1fr 1.4fr;gap:8px;padding:8px 10px;background:rgba(255,255,255,.97);backdrop-filter:blur(8px);border-top:1px solid var(--line)}
.mbar a{text-align:center;padding:12px;border-radius:12px;font-weight:800;font-size:13px}
.mb-tel{background:var(--navy);color:#fff}
.mb-form{background:linear-gradient(135deg,var(--cyan),var(--cyan-d));color:#fff}
@media(max-width:900px){.mbar{display:grid}.pagetop{bottom:76px}}
"""

APP_JS = r"""// reveal on scroll
const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('vis');io.unobserve(e.target)}})},{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
// header solid + pagetop
const hd=document.getElementById('hd'),pt=document.querySelector('.pagetop');
function onScroll(){const y=window.scrollY;if(hd){hd.classList.toggle('solid',y>60||!document.querySelector('.hero'))}if(pt){pt.classList.toggle('show',y>500)}}
// pages without hero: header always solid
if(!document.querySelector('.hero')&&hd){hd.classList.add('solid')}
window.addEventListener('scroll',onScroll,{passive:true});onScroll();
// close mobile menu on link tap
document.querySelectorAll('.mnav a').forEach(a=>a.addEventListener('click',()=>document.body.classList.remove('mopen')));
"""


def build_assets() -> None:
    (ROOT / "assets").mkdir(exist_ok=True)
    (ROOT / "assets" / "style.css").write_text(CSS, encoding="utf-8")
    (ROOT / "assets" / "app.js").write_text(APP_JS, encoding="utf-8")


def main() -> None:
    build_assets()
    build_top()
    build_services()
    build_works()
    build_company()
    build_column()
    build_contact()
    build_thanks()
    build_privacy()
    print("built: index, services, works, company, column(+%d), contact, thanks, privacy" % len(ARTICLES))


if __name__ == "__main__":
    main()
