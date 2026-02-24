---
# Template for Olivín Stromeček product pages
# Variables available:
# PRODUCT_NAME, SECOND_NAME, PRODUCT_CODE, PRICE, BUY_PRICE, HERO_IMAGE,
# URL, SEO_TITLE, SEO_DESC, FB_TITLE, FB_DESC, SHORT_DESC, H1, STORY_HTML,
# PRIMARY_BENEFIT, SECONDARY_BENEFIT,
# GALLERY_COLLECTION_HTML, GALLERY_DETAIL_HTML,
# MINERALS_HTML, PRINOS_HTML, PLANTING_HTML, RITUAL_HTML, CARE_HTML,
# SAFETY_HTML, CONTACT_HTML, FOOTPATHS_HTML, SOURCES_HTML,
# EN_INTRO_HTML, EN_GALLERY_COLLECTION_HTML, EN_GALLERY_DETAIL_HTML,
# EN_MINERALS_HTML, EN_PRINOS_HTML, EN_PLANTING_HTML, EN_RITUAL_HTML,
# EN_CARE_HTML, EN_SAFETY_HTML, EN_CONTACT_HTML, EN_FOOTPATHS_HTML,
# EN_SOURCES_HTML,
# JSON_LD
---


**{{PRODUCT_NAME}}**

**Název produktu**: {{PRODUCT_NAME}}

**2.název produktu**: {{SECOND_NAME}}

**Číslo produktu**: {{PRODUCT_CODE}}

**Cena (blank)**: {{PRICE}}

**Nákupní cena (blank)**: {{BUY_PRICE}}

Obrázek 603x800px (detailní „hero") ano

Obrázek 277x330px (náhledový „pozadi") ano

Označení výrobku: {{PRODUCT_CODE}}

**Title (pro vyhledávače):** {{SEO_TITLE}}

**Popis** (pro vyhledávače, 150 znaků): {{SEO_DESC}}

**Vlastní URL**: {{URL}}

**Title (pro FB):** {{FB_TITLE}}

**Popis** (pro FB, do 200 znaků): {{FB_DESC}}

Obrázek pro FB (1200x628px) ano

Připojené produkty ano (orgonity)

Podobné produkty ano (Olivínová Štěstíčka)

**Exportní feedy - Globální nastavení:**

Název produktu (tag PRODUCTNAME, příp. title, name): {{SEO_TITLE}}

Rozšířený název produktu (tag PRODUCT): {{SECOND_NAME}}

Popis produktu (tag DESCRIPTION): {{SHORT_DESC}}

Obrázek pro feed (tag IMGURL, 425x440px): ano

Dárek (tag GIFT): vonavý dáreček

**Krátký popis produktu (300 znaků)**

{{SHORT_DESC}}

**Detailní popis produktu:**

**<!-- ✅ Začátek stránky -->**

<div class="product-detail-description">

<!-- Sticky Language Switcher -->

<nav aria-label="Přepínač jazyka" class="lang-bar-sticky" style="position:sticky; top:0; z-index:100; background:#f0fff0; border:2px solid #0c7c00; border-radius:8px; padding:.6em .9em; margin:.75em 0; box-shadow:0 2px 8px rgba(0,0,0,.08); display:flex; align-items:center; justify-content:center; gap:.75em; font-weight:bold;">

<label for="language-switcher" style="margin:0;" aria-label="Zvol jazyk stránky">🌍&nbsp;<span style="white-space:nowrap;">Jazyk / Language:</span></label>

<select id="language-switcher" aria-label="Změna jazyka" style="font-weight:600; padding:0.4em 0.8em; border-radius:6px; border:1px solid #0c7c00;">

<option value="cs">🇨🇿&nbsp;Čeština</option>

<option value="en">🇬🇧&nbsp;English</option>

</select>

</nav>

<!-- Český text -->

<div data-lang="cs" lang="cs" role="main">

<progress id="reading-progress" value="0" max="100" aria-hidden="true"></progress>

<a href="#uvod" class="sr-only">Přeskočit na hlavní obsah</a>

<h1 class="sr-only">{{H1}}</h1>

<!-- Úvod -->

<section id="uvod" class="section-box section-warm">

<h2><span aria-hidden="true">🌟&nbsp;</span>Čím si zamiluješ {{PRODUCT_NAME}}?</h2>

<ul style="list-style:'✅ '; padding-left:1.5em;">

<li>Ručně drátovaný Stromeček Štěstí od Arllette.</li>

<li>Jedinečný základ – český olivínovec (peridotit) z lomu Smrčí.</li>

<li>Přináší energii elementů Země, Dřeva, Vzduchu, Ohně, Kovu a Éteru.</li>

<li>✨ ideální talisman pro <strong>{{PRIMARY_BENEFIT}}</strong>.</li>

<li>💞 <strong>dárek s příběhem, který roste</strong> – dárková <strong>krabička</strong>, <strong>certifikát</strong> a <strong>Stromové dvojče vysazené</strong> v příbramských lesích.</li>

<li>🌱 jemná podpora <strong>{{SECONDARY_BENEFIT}}</strong>.</li>

</ul>

</section>

<!-- Rozcestník -->

<nav class="section-box section-highlight" aria-label="Rychlá navigace">

<h2><span aria-hidden="true">🔍️&nbsp;</span>Co Tě nyní zajímá?</h2>

<p style="margin-top:0.75em;">Prozkoumej {{PRODUCT_NAME}} ze všech stran:</p>

<ul style="list-style:none; padding-left:0;">

<li><span aria-hidden="true">🌳&nbsp;</span><a href="#symbolika">Symbolika a příběh Olivínu</a></li>

<li><span aria-hidden="true">💎&nbsp;</span><a href="#mineral">Vlastnosti minerálů</a></li>

<li><span aria-hidden="true">✨&nbsp;</span><a href="#prinos">Čím Tě podpoří?</a></li>

<li><span aria-hidden="true">🌲&nbsp;</span><a href="#les">Výsadba živého dvojčete</a></li>

<li><span aria-hidden="true">🧘&nbsp;</span><a href="#ritual">Rituály s {{PRODUCT_NAME}}</a></li>

<li><span aria-hidden="true">💗 &nbsp;</span> <a href="#pece">Péče o Tvé Štěstíčko</a></li>

<li><span aria-hidden="true">🛡️&nbsp;</span> <a href="#bezpecnost">Bezpečné zacházení talismanem</a></li>

</ul>

</nav>

<!-- Symbolika -->

<section id="symbolika" class="section-box section-warm flex-wrap" aria-labelledby="nadpis-symbolika">

<h2 id="nadpis-symbolika"><span aria-hidden="true">🌳&nbsp;</span>Symbolika Stromečku Štěstí</h2>

<p style="margin-top: 0.75em;"><strong>Strom života</strong> je uctíván mnoha kulturami jako <strong>symbol věčného života a znovuzrození</strong>. Propojuje <strong>minulost</strong> (kořeny), <strong>přítomnost</strong> (kmen) a <strong>budoucnost</strong> (koruna).</p>

<p><strong>Kořeny</strong> čerpají <strong>moudrost předků</strong>, sílu <a href="/element-zeme">Země</a> i <a href="/element-voda">Vody</a>. <strong>Kmen</strong> představuje <strong>myšlenky, slova i činy</strong>, a vede jejich energii vzhůru. <strong>Koruna</strong> se větví ke <strong>květům, listům a plodům</strong>, které symbolizují budoucí výsledky naší každodenní práce.</p>

<p>Miniaturní Stromeček Štěstí s minerály symbolizuje propojení živé a neživé přírody, logické i emoční roviny života. Jeho příběh se promítá do hmotného světa jeho propojením s <strong>živým <a href="/kategorie/strom-pro-strom/">Stromovým dvojčetem</a></strong>, vysazeným v českých lesích.</p>

<h2><span aria-hidden="true">📜&nbsp;</span>Příběh {{PRODUCT_NAME}}</h2>

{{STORY_HTML}}

</section>

<!-- Fotogalerie kolekce -->

<section id="galerie-stesticka" class="section-box" aria-labelledby="nadpis-galerie">

<h2 id="nadpis-galerie"><span aria-hidden="true">📷&nbsp;</span>Rodina Olivínových Štěstíček</h2>

<figure style="margin:0 auto 0; max-width:350px;">

<img src="{{FAMILY_GALLERY_LEAD_IMAGE}}" alt="Rodina Olivínových Štěstíček" class="image-rounded" width="350" height="350" loading="lazy" decoding="async" />

</figure>

<br>

<p>Zajímají Tě <strong>sourozenci {{PRODUCT_NAME}}</strong>? Poslechni si i jejich příběh…</p>

<p class="small-text" style="text-align: center;">…stačí se dotknout jejich jména a otevře se Ti cesta dál…</p>

<div id="galerie-oliviny" class="swiper gallery-swiper">

<div class="swiper-wrapper">

{{GALLERY_COLLECTION_SLIDES}}

</div>

<!-- Ovládací šipky Swiper -->

<button class="swiper-button-prev" aria-controls="galerie-oliviny" aria-label="Předchozí foto">&nbsp;</button>

<button class="swiper-button-next" aria-controls="galerie-oliviny" aria-label="Další foto">&nbsp;</button>

<div class="swiper-pagination" aria-hidden="true"></div>

</div>

</section>

<!-- Minerály -->

<section id="mineral" class="section-box section-highlight flex-wrap" aria-labelledby="nadpis-mineral">

<div class="flex-item">

<h2 id="nadpis-mineral"><span aria-hidden="true">💎&nbsp;</span>Minerály {{PRODUCT_NAME}}</h2>

<div class="flex-item" style="text-align: center;"><img src="{{MINERAL_LEAD_IMAGE}}" alt="Koruna {{PRODUCT_NAME}}" class="image-rounded" width="350" height="350" loading="lazy" decoding="async" />

<p class="small-text">Koruna {{PRODUCT_NAME}}</p>

</div>

<p>Tento <a href="/stesticka"><strong>miniaturní Stromeček Štěstí </strong></a> čerpá sílu elementů <a href="/system-zivly"><strong>Země, Dřeva, Ohně, Kovu a Éteru</strong></a>, a svými minerály podporuje energetický <a href="/system-cakry">systém čaker</a>:</p>

<p><span aria-hidden="true">💎&nbsp;</span> <strong>{{MINERAL_1_NAME}}</strong> {{MINERAL_1_DESC}}</p>

<p><span aria-hidden="true">💎&nbsp;</span> <strong>{{MINERAL_2_NAME}}</strong> {{MINERAL_2_DESC}}</p>

<p><span aria-hidden="true">💎&nbsp;</span> <strong>{{MINERAL_3_NAME}}</strong> {{MINERAL_3_DESC}}</p>

<p><span aria-hidden="true">🔶&nbsp;</span> <strong>Měď</strong> harmonizuje celý systém čaker silou elementů <a href="/element-eter">Éteru</a> a <a href="/element-kov">Kovu</a>. Rozpouští energetické blokády, tiší emoční výkyvy, tlumí strach a přináší chuť do života. Posiluje koncentraci, sebedůvěru a sebevědomí. Oživuje fantazii, smyslnost a podporuje plodnost fyzickou i uměleckou.</p>

<p class="small-text">Více o energii kamenů najdeš <a href="/energie-kamenu"><strong>v tomto článku</strong></a><span aria-hidden="true">📜</span>.</p>

</div>

</section>

<!-- Fotogalerie talismanu (detail) -->

<section id="galerie-detaily" class="section-box" aria-labelledby="nadpis-galerie-detaily">

<h2 id="nadpis-galerie-detaily"><span aria-hidden="true">📷&nbsp;</span>Proměnlivost {{PRODUCT_NAME}}</h2>

<p style="margin-top: 0.75em;">Prohlédni si {{PRODUCT_NAME}} v harmonii s přírodou <span aria-hidden="true">💚</span></p>

<div id="galerie-detail" class="swiper gallery-swiper">

	<div class="swiper-wrapper">

	{{GALLERY_DETAIL_SLIDES}}

	</div>

	<button class="swiper-button-prev" aria-controls="galerie-detail" aria-label="Předchozí foto">&nbsp;</button>

	<button class="swiper-button-next" aria-controls="galerie-detail" aria-label="Další foto">&nbsp;</button>

	<div class="swiper-pagination" aria-hidden="true"></div>

</div>

</section>

<!-- Přínos -->

<section id="prinos" class="section-box section-highlight flex-wrap" aria-labelledby="nadpis-prinos">

<div class="flex-item">

	<h2 id="nadpis-prinos"><span aria-hidden="true">✨&nbsp;</span>Co Ti {{PRODUCT_NAME}} přináší?</h2>

	<p>Svou kombinací barev a minerálů je jemným <strong>podporujícím energetickým talismanem</strong>, který harmonizuje <a href="/system-cakry"><strong>1. kořenovou, 2. sakrální a 4. srdeční čakru</strong></a> silou <a href="/system-zivly"><strong>elementů Země, Dřeva, Kovu, Ohně a Éteru</strong></a>.</p>

	<p>{{PRINOS_DESC}}</p>

</div>

</section>

<!-- Výsadba Dvojčete -->

<section id="les" class="section-box section-warm flex-wrap" aria-labelledby="nadpis-vysadba">

<div class="flex-item">

	<h2 id="nadpis-vysadba"><span aria-hidden="true">🌳&nbsp;</span>Výsadba Stromového dvojčete</h2>

	<div class="flex-item" style="text-align: center;">

		<img src="{{PLANTING_IMAGE}}" alt="S láskou sázíme stromy" class="image-rounded" width="350" height="350" loading="lazy" decoding="async" />

		<p class="small-text">S láskou sázíme stromy</p>

	</div>

	<p style="margin-top: 0.75em;">Les tvoří rodina stromů, která je pevně propojená kořeny. Těmi se navzájem podporují, posílají si živiny i varování. I kamenné <a href="/stromy"><strong>Stromy Života</strong></a> se rozrůstají v <strong>Magický les splněných přání</strong>, ve kterém jsou <a href="/strom-pro-strom">propojené s živými stromy</a> v českých lesích.</p>

	<h3><strong>Jak toto propojení vzniká? Výsadbou!</strong></h3>

	<figure style="margin:0 auto 0; max-width:450px;">

		<img src="{{PLANTING_CERT_IMAGE}}" alt="Certifikát" class="image-rounded" loading="lazy" decoding="async" />

		<figcaption class="small-text" style="text-align: center;">Certifikát dvojčat</figcaption>

	</figure>

	<p style="margin-top: 0.75em;">Pro rodinu {{PRODUCT_NAME}} jsme jejich <a href="/strom-pro-strom">Stromová dvojčata</a> nechali vysadit od <a href="https://homefortrees.com/premenili-jsme-pole-na-les-o-3-000-stromech" target="_blank" rel="noopener noreferrer">Home for Trees v Mokrovratech na příbramsku</a>.</p>

	<ul>

		<li><strong><span aria-hidden="true">🌱&nbsp;</span>Zakoupení sazenice:</strong> {{SAPLING_DATE}}</li>

		<li><strong><span aria-hidden="true">🌲&nbsp;</span>Datum vysazení:</strong> {{PLANT_DATE}}</li>

		<li><strong><span aria-hidden="true">📍&nbsp;</span>Najdeš ho na <a href="{{PLANT_GPS_URL}}">těchto GPS souřadnicích</a></strong>.</li>

		<li><strong><span aria-hidden="true">📸&nbsp;</span>Pošli nám fotku, když půjdeš kolem ❤️</strong></li>

	</ul>

</div>

</section>

<!-- Rituály s talismanem -->

<section id="ritual" class="section-box section-highlight" aria-labelledby="nadpis-ritual">

	<h2 id="nadpis-ritual"><span aria-hidden="true">🧘&nbsp;</span>Rituály s {{PRODUCT_NAME}}</h2>

	<figure style="margin:0 auto 0; max-width:350px;">

		<img src="{{RITUAL_IMAGE}}" alt="Rituál" class="image-rounded" width="350" height="350" loading="lazy" decoding="async" />

		<figcaption class="small-text" style="text-align: center;">Meditující {{PRODUCT_NAME}}</figcaption>

	</figure>

	<p style="margin-top: 0.75em;">Zajímá Tě, s jakými rituály Ti může {{PRODUCT_NAME}} pomoci? S jakýmkoliv, ke kterým ho přizveš! Věda i duchovní tradice se shodují, že klidná pozornost – ať jí říkáme rituál, meditace či mindfulness – prospívá tělu, mysli i duši. Vyzkoušej si tuto krátkou praxi – a pokud se Ti zalíbí, dovol si ji zařadit do svého života. Snadno si ji upravíš podle sebe. 😊</p>

	<article class="flex-item block-article" style="background: #fcf8f2;">

		<h3><span aria-hidden="true">☮️&nbsp;</span>Nadechni se Ohně (<span aria-hidden="true">⏱️&nbsp;</span>2 min)</h3>

		<ul style="margin:0 0 0 1rem; line-height:1;">

			<li><strong>Zastav se.</strong> Polož {{PRODUCT_NAME}} před sebe, nebo si ho vezmi do levé dlaně. Pravou dlaň přilož nad srdce (<a href="/4-cakra">4. srdeční čakra</a>).</li>

			<li><strong>Dýchej.</strong> Zavři oči, <strong>nadechni se na 4</strong> doby a pomalu <strong>vydechuj na 6</strong> dob.</li>

			<li><strong>Vizualizuj.</strong> Představ si, jak se s nádechem do Tvého hrudníku vlévá <strong>zlaté světlo</strong>.</li>

			<li><strong>Třikrát opakuj</strong>.</li>

		</ul>

	</article>

	<p class="small-text" style="margin-top: 0.75em;">Tento krátký rituál si uprav podle svých potřeb a opakuj i několikrát denně.</p>

</section>

<!-- Péče o talisman -->

<section id="pece" class="section-box section-warm" aria-labelledby="nadpis-pece">

	<h2 id="nadpis-pece"><span aria-hidden="true">🫶&nbsp;</span>Péče o {{PRODUCT_NAME}}</h2>

	<div class="flex-wrap" style="gap: 1.5em; justify-content: space-between;">

		<article class="flex-item"> <img src="/fotky4514/blog/Pece/Cisteni_400.jpg" alt="Mechanické čištění" class="image-rounded" width="200" height="200" loading="lazy" decoding="async"/>

			<h3><span aria-hidden="true">🫧&nbsp;</span>Mechanické čištění</h3>

			<p>Kamenné lístky čisti jemně jako listy pokojových rostlin – nám se osvědčil měkký kartáček. <strong>{{PRODUCT_NAME}} můžeš krátce opláchnout</strong>, ale nenechávej ho dlouho ve vodě.</p>

		</article>

		<article class="flex-item"> <img src="/fotky4514/blog/Pece/Nabijeni_400.jpg" alt="Energetické nabíjení" class="image-rounded" width="200" height="200" loading="lazy" decoding="async"/>

			<h3><span aria-hidden="true">✨&nbsp;</span>Energetické čištění</h3>

			<p>Minerály stále pracují s energií ve svém okolí, proto si občas potřebují odpočinout. <strong>Peridotite can yellow in direct sun</strong>, proto {{PRODUCT_NAME}} nabíjej na <strong>nepřímém slunečním světle</strong> nebo <strong>při úplňku</strong>.</p>

		</article>

		<article class="flex-item"> <img src="/fotky4514/blog/Pece/TrollTip_400.jpg" alt="Trollův tip" class="image-rounded" width="200" height="200" loading="lazy" decoding="async"/>

			<h3><span aria-hidden="true">🌀&nbsp;</span>Trollův tip – orgonit</h3>

			<p>Pokud chceš mít {{PRODUCT_NAME}} stále energeticky čistý a plný sil, polož ho na <strong>orgonitovou podložku</strong> nebo do blízkosti orgonitu.</p>

		</article>

	</div>

	<p class="small-text" style="margin-top: 0.75em;">Zajímá Tě očistný rituál vykuřování? Prohlédni si <a href="/vune-lesa">Vůně lesa</a>.</p>

</section>

<!-- Bezpečnostní doporučení -->

<section id="bezpecnost" class="section-box section-highlight" aria-labelledby="nadpis-bezpecnost">

	<div class="flex-wrap" style="gap: 1.5em;">

		<article class="flex-item section-safe" style="flex-basis: 48%; min-width: 220px; padding: 1em;">

			<h3 style="color: #2e7d32;"> <span aria-hidden="true">✅&nbsp;</span>Bezpečné zacházení</h3>

			<ul>

				<li>Vhodné na oltář, poličku i stůl.</li>

				<li>Vhodné k meditaci a vědomé práci se záměrem.</li>

				<li>Polož na podložku, která ochrání podklad před poškrábáním.</li>

				<li>Ideální je trvalé místo bez častého přenášení.</li>

			</ul>

		</article>

		<article class="flex-item section-risk" style="flex-basis: 48%; min-width: 220px; padding: 1em;">

			<h3 style="color: #c62828;"> <span aria-hidden="true">⚠️&nbsp;</span>Rizikové zacházení</h3>

			<ul>

				<li>Nevhodné pro děti do 6 let – ostré drátky a malé komponenty.</li>

				<li>Nepatří do vody ani vlhkého prostředí.</li>

				<li>Kámen je tvrdý a křehký – může se při pádu poškodit.</li>

				<li>Drátek se opakovaným ohýbáním láme – tvaruj s opatrností.</li>

			</ul>

		</article>

	</div>

</section>

<!-- Napiš nám -->

<section class="section-box section-highlight" aria-labelledby="nadpis-kontaktuj">

	<div class="flex-wrap" style="align-items: center; gap: 1.5em;">

		<article class="flex-item" style="flex: 1.6 1 400px;">

			<h2 id="nadpis-kontaktuj"><span aria-hidden="true">🔍&nbsp;</span>Chceš vědět víc?</h2>

			<p style="margin-top: 0.75em;">Nacházíš u {{PRODUCT_NAME}} inspiraci ke splnění vlastního přání, nebo k dárku pro své blízké?</p>

			<p>Chybí Ti tu nějaká <strong>informace</strong> nebo je třeba cokoliv opravit?</p>

			<p><strong>Každou otázku i postřeh vítáme!</strong> Kdykoliv <strong><a href="/kontakt">napiš či zavolej</a></strong>, nebo si s námi popovídej přes <strong><a href="https://wa.me/{{CONTACT_PHONE}}">WhatsApp</a></strong> či <strong><a href="https://www.facebook.com/groups/443898744849082">Messenger</a></strong>. 😊</p>

			<p class="small-text" style="margin-top: 1em;">P.S. Když na webu objevíš chybku a dáš nám vědět, máš u nás slevu! Děkujeme, že s námi pečuješ o Magický les <span aria-hidden="true">🍀</span>.</p>

		</article>

		<div class="flex-item" style="flex: 1.4 1 200px; text-align: center;"><img src="/fotky4514/blog/Pece/Troll_pozadi_800-min.jpg" alt="Vychechtaný Troll – Tvůj průvodce Magickým lesem" loading="lazy" class="avatar-circle" style="max-width: 100%; width: 200px; height: auto;" />

			<p class="small-text">Jsem <strong><a href="/troll-2">Vychechtaný Troll</a></strong>,<br> Tvůj průvodce Magickým lesem.</p>

		</div>

	</div>

</section>

<!-- Kudy dál -->

<section class="section-box section-warm" aria-labelledby="nadpis-cesty">

{{FOOTPATHS_HTML}}

</section>

<!-- GPSR a naši dodavatelé -->

<section id="sources" class="section-box section-highlight" aria-labelledby="nadpis-gpsr"><details open>

	<summary id="nadpis-gpsr"><span aria-hidden="true">📚&nbsp;</span>GPSR a naši dodavatelé ⤵️</summary>

	<div style="margin-top: 1.2em;">

		<p style="margin-top: 0.75em;">S radostí, a v souladu s <strong>nařízením GPSR</strong> (<em>General Product Safety Regulation</em>), tady uvádíme veškeré informace o původu talismanu {{PRODUCT_NAME}}. Je to Stromeček Štěstí s minerály, určený pro dekorativní účely v interiéru. Ačkoliv to zní zvláštně, musíme uvést, že tento talisman <strong>není určen ke konzumaci, jako hračka pro děti ani jako náhrada odborné zdravotní péče.</strong></p>

		<p><strong>{{PRODUCT_NAME}} jsme vlastnoručně vyrobili v našem rodinném ateliéru</strong>.</p>

		<ul>

			<li><strong>Výrobce:</strong>&nbsp;{{MANUFACTURER_NAME}}</li>

			<li><strong>E-mail:&nbsp;</strong><a href="mailto:{{CONTACT_EMAIL}}"><u>{{CONTACT_EMAIL}}</u></a></li>

			<li><strong>Telefon:</strong>&nbsp;{{CONTACT_PHONE}}</li>

			<li><strong>Adresa:</strong>&nbsp;{{MANUFACTURER_ADDRESS}}</li>

		</ul>

		<p>Tímto jsme naplnili zákonné požadavky. Citujeme zdroje informací níže.</p>

		<ul>

			<li>DOMELI [online e-shop]. c2024 [citováno 2024-08-27]. Dostupné z: <a href="https://www.domeli.cz" target="_blank" rel="noopener">https://www.domeli.cz</a></li>

			<li>KREPERÁT, Josef Pavel. <em>Skrytá moc drahých kamenů a jejich vliv na naše duševní a fyzické zdraví</em>. Praha: Granit, 2003. ISBN 80-7296-020-2.</li>

			<li>Wikipedie: Otevřená encyklopedie [online]. c2024 [citováno 2024-08-27]. Dostupné z: <a href="https://cs.wikipedia.org" target="_blank" rel="noopener">https://cs.wikipedia.org</a></li>

		</ul>

		<p class="small-text" style="margin-top: 1em;"><span aria-hidden="true">📅&nbsp;</span><strong>Stránka vytvořena:&nbsp;</strong>{{PAGE_CREATED}}<br><span aria-hidden="true">🔄&nbsp;</span> <strong>Poslední aktualizace:&nbsp;</strong>{{PAGE_UPDATED}}</p>

	</div>

</details>

</section>

</div>

<!-- ✅ Začátek AJ stránky -->


<div data-lang="en" lang="en" role="region" aria-labelledby="nadpis-intro-en">

	<section id="uvod-en" class="section-box section-warm">

		<h2><span aria-hidden="true">🌟&nbsp;</span>Why will you fall in love with {{PRODUCT_NAME}}?</h2>

		{{EN_INTRO_PARAGRAPHS}}

	</section>

	<section id="galerie-stesticka-en" class="section-box" aria-labelledby="nadpis-galerie-en">

		<h2 id="nadpis-galerie-en"><span aria-hidden="true">📷&nbsp;</span>The {{PRODUCT_NAME}} family</h2>

		<div id="galerie-oliviny-en" class="swiper gallery-swiper">

			<div class="swiper-wrapper">

			{{EN_GALLERY_COLLECTION_SLIDES}}

			</div>

			<button class="swiper-button-prev" aria-controls="galerie-oliviny-en" aria-label="Previous photo">&nbsp;</button>

			<button class="swiper-button-next" aria-controls="galerie-oliviny-en" aria-label="Next photo">&nbsp;</button>

			<div class="swiper-pagination" aria-hidden="true"></div>

		</div>

	</section>

	<section id="mineral-en" class="section-box section-highlight flex-wrap" aria-labelledby="nadpis-mineral-en">

		<div class="flex-item">

			<h2 id="nadpis-mineral-en"><span aria-hidden="true">💎&nbsp;</span>Minerals of {{PRODUCT_NAME}}</h2>

			<div class="flex-item" style="text-align: center;"><img src="{{EN_MINERAL_LEAD_IMAGE}}" alt="Crown of {{PRODUCT_NAME}}" class="image-rounded" width="350" height="350" loading="lazy" decoding="async" />

			<p class="small-text">Crown of {{PRODUCT_NAME}}</p>

			</div>

			<p>{{EN_MINERAL_1_NAME}} {{EN_MINERAL_1_DESC}}</p>

			<p>{{EN_MINERAL_2_NAME}} {{EN_MINERAL_2_DESC}}</p>

			<p>{{EN_MINERAL_3_NAME}} {{EN_MINERAL_3_DESC}}</p>

		</div>

	</section>

	<section id="galerie-detaily-en" class="section-box" aria-labelledby="nadpis-galerie-detaily-en">

		<h2 id="nadpis-galerie-detaily-en"><span aria-hidden="true">📷&nbsp;</span>The many faces of {{PRODUCT_NAME}}</h2>

		<div id="galerie-detail-en" class="swiper gallery-swiper">

			<div class="swiper-wrapper">

			{{EN_GALLERY_DETAIL_SLIDES}}

			</div>

			<button class="swiper-button-prev" aria-controls="galerie-detail-en" aria-label="Previous photo">&nbsp;</button>

			<button class="swiper-button-next" aria-controls="galerie-detail-en" aria-label="Next photo">&nbsp;</button>

			<div class="swiper-pagination" aria-hidden="true"></div>

		</div>

	</section>

	<section id="prinos-en" class="section-box section-highlight flex-wrap" aria-labelledby="nadpis-prinos-en">

		<div class="flex-item">

			<h2 id="nadpis-prinos-en"><span aria-hidden="true">✨&nbsp;</span>What does {{PRODUCT_NAME}} bring you?</h2>

			<p>{{EN_PRINOS_DESC}}</p>

		</div>

	</section>

	<section id="les-en" class="section-box section-warm flex-wrap" aria-labelledby="nadpis-vysadba-en">

		<div class="flex-item">

			<h2 id="nadpis-vysadba-en"><span aria-hidden="true">🌳&nbsp;</span>Planting the Tree Twin</h2>

			<p>{{EN_PLANTING_PARAGRAPHS}}</p>

			<ul>

				<li><strong>Sapling purchased:</strong> {{EN_SAPLING_DATE}}</li>

				<li><strong>Planting date:</strong> {{EN_PLANT_DATE}}</li>

				<li><strong>Find it on:</strong> <a href="{{EN_PLANT_GPS_URL}}">map</a></li>

			</ul>

		</div>

	</section>

	<section id="ritual-en" class="section-box section-highlight" aria-labelledby="nadpis-ritual-en">

		<h2 id="nadpis-ritual-en"><span aria-hidden="true">🧘&nbsp;</span>Rituals with {{PRODUCT_NAME}}</h2>

		<p>{{EN_RITUAL_PARAGRAPHS}}</p>

	</section>

	<section id="pece-en" class="section-box section-warm" aria-labelledby="nadpis-pece-en">

		<h2 id="nadpis-pece-en"><span aria-hidden="true">🫶&nbsp;</span>Caring for {{PRODUCT_NAME}}</h2>

		<p>{{EN_CARE_PARAGRAPHS}}</p>

	</section>

	<section id="bezpecnost-en" class="section-box section-highlight" aria-labelledby="nadpis-bezpecnost-en">

		<h2 id="nadpis-bezpecnost-en"><span aria-hidden="true">🛡️&nbsp;</span>Safe use</h2>

		<p>{{EN_SAFETY_PARAGRAPHS}}</p>

	</section>

	<section id="kontakt-en" class="section-box section-warm" aria-labelledby="nadpis-kontaktuj-en">

		<h2 id="nadpis-kontaktuj-en"><span aria-hidden="true">🔍&nbsp;</span>Want to know more?</h2>

		<p>{{EN_CONTACT_PARAGRAPHS}}</p>

	</section>

	<section id="cesty-en" class="section-box section-highlight" aria-labelledby="nadpis-cesty-en">

		<h2 id="nadpis-cesty-en"><span aria-hidden="true">🌎&nbsp;</span>Footpaths through the Magical Forest</h2>

		<ul>

			<li><a href="/blog">Tales of the Magical Forest</a></li>

			<li><a href="/stromy-zvirata">Trees of Life and shamanic Animals</a></li>

			<li><a href="/talismany">Chakra talismans</a></li>

		</ul>

	</section>

</div></div>

<script type="application/ld+json">
{
	"@context": "https://schema.org",
	"@graph": [
		{
			"@type": "Organization",
			"@id": "{{ORG_URL}}#brand",
			"name": "{{MANUFACTURER_NAME}}",
			"url": "{{ORG_URL}}",
			"logo": {"@type":"ImageObject","url":"{{ORG_LOGO}}","width":800,"height":800},
			"contactPoint": {"@type":"ContactPoint","contactType":"customer support","email":"{{CONTACT_EMAIL}}","telephone":"{{CONTACT_PHONE}}","availableLanguage":["cs","sk","en"]}
		},
		{
			"@type": "WebPage",
			"@id": "{{PAGE_URL}}#webpage",
			"url": "{{PAGE_URL}}",
			"name": "{{SEO_TITLE}}",
			"inLanguage": "cs",
			"primaryImageOfPage": {"@type":"ImageObject","url":"{{HERO_IMAGE}}"}
		},
		{
			"@type": "Product",
			"@id": "{{PAGE_URL}}#product",
			"name": "{{PRODUCT_NAME}}",
			"description": "{{SHORT_DESC}}",
			"url": "{{PAGE_URL}}",
			"image": {{JSON_IMAGES}},
			"sku": "{{PRODUCT_CODE}}",
			"brand": {"@type":"Brand","name":"{{MANUFACTURER_NAME}}"},
			"offers": {"@type":"Offer","url":"{{PAGE_URL}}","price":"{{PRICE}}","priceCurrency":"{{PRICE_CURRENCY}}","availability":"{{AVAILABILITY}}","inventoryLevel":{"@type":"QuantitativeValue","value":{{INVENTORY}}}}
		}
	]
}
</script>
