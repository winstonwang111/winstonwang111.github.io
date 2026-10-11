---
layout: page
permalink: /cv/
title: CV
nav: true
nav_order: 5
cv_pdf: /assets/pdf/example_pdf.pdf # you can also use external links here
description: Education, professional experience, publications, and research interests / 教育背景、工作经历、论文发表与研究方向
toc:
  sidebar: left
---

{% if page.cv_pdf %}
<p><a href="{{ page.cv_pdf | relative_url }}" target="_blank" rel="noopener noreferrer">Download CV / 下载简历</a></p>
{% endif %}

{% for section in site.data.cv.cv.sections %}
<section class="card mt-3 p-3">
  <h2>{{ section[0] | escape }}</h2>
  {% for entry in section[1] %}
  <div class="mb-3">
    {% if entry.label %}
    <h3>{% if entry.url %}<a href="{{ entry.url | escape }}">{{ entry.label | escape }}</a>{% else %}{{ entry.label | escape }}{% endif %}</h3>
    {% endif %}
    <p lang="en">{{ entry.details | escape }}</p>
    {% if entry.translation %}<p lang="zh-CN">{{ entry.translation | escape }}</p>{% endif %}
    {% if entry.highlights %}
    <ul>
      {% for highlight in entry.highlights %}
      <li><span lang="en">{{ highlight.english | escape }}</span><br><span lang="zh-CN">{{ highlight.chinese | escape }}</span></li>
      {% endfor %}
    </ul>
    {% endif %}
  </div>
  {% endfor %}
</section>
{% endfor %}
