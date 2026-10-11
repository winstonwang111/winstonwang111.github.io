---
layout: page
permalink: /cv/
title: CV
nav: true
nav_order: 5
cv_pdf: /assets/pdf/Winston_Wang_CV.pdf
description: Education, professional experience, publications, and research interests / 教育背景、工作经历、论文发表与研究方向
toc:
  sidebar: left
_styles: |
  .cv-content { font-size: 1rem; line-height: 1.65; }
  .cv-content h2 { font-size: 1.35rem; font-weight: 600; margin-bottom: 1rem; }
  .cv-entry-title { font-size: 1.05rem; font-weight: 600; line-height: 1.45; margin-bottom: 0.45rem; }
  .cv-content p { margin-bottom: 0.55rem; }
  .cv-content li { margin-bottom: 0.5rem; }
  .cv-entry { margin-bottom: 1.4rem; }
  .cv-period { font-size: 0.9rem; opacity: 0.8; margin-bottom: 0.5rem; }
---

{% if page.cv_pdf %}
<p><a href="{{ page.cv_pdf | relative_url }}" target="_blank" rel="noopener noreferrer">Download CV / 下载简历</a></p>
{% endif %}

<div class="cv-content">
{% for section in site.data.cv.cv.sections %}
<section class="card mt-3 p-3">
  <h2>{{ section[0] | escape }}</h2>
  {% for entry in section[1] %}
  <div class="cv-entry">
    {% if entry.label %}
    <div class="cv-entry-title">{% if entry.url %}<a href="{{ entry.url | escape }}">{{ entry.label | escape }}</a>{% else %}{{ entry.label | escape }}{% endif %}</div>
    {% endif %}
    {% if entry.period %}<p class="cv-period">{{ entry.period | escape }}</p>{% endif %}
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
</div>
