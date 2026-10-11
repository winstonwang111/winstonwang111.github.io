from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
import pypdfium2 as pdfium
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output/pdf'
OUT.mkdir(parents=True, exist_ok=True)
pdfmetrics.registerFont(TTFont('Sans', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('SansBold', 'C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFont(TTFont('Chinese', 'C:/Windows/Fonts/msyh.ttc', subfontIndex=0))
pdfmetrics.registerFont(TTFont('ChineseBold', 'C:/Windows/Fonts/msyhbd.ttc', subfontIndex=0))
TARGET = OUT / 'Winston_Wang_Minimal_CV_EN_CN.pdf'
c = canvas.Canvas(str(TARGET), pagesize=A4)
c.setTitle('Winston (Ze) Wang | Bilingual Curriculum Vitae')
c.setAuthor('Winston (Ze) Wang')
W,H=A4
LEFT=44
WIDTH=W-88
y=0
lang='en'

def text(s, size=9, bold=False, color='#303033', gap=4):
    global y
    font=('Chinese' if lang=='zh' else 'Sans') + ('Bold' if bold else '')
    style=ParagraphStyle('body',fontName=font,fontSize=size,leading=size*1.38,textColor=HexColor(color))
    p=Paragraph(s,style)
    _,height=p.wrap(WIDTH,1000)
    p.drawOn(c,LEFT,y-height)
    y-=height+gap

def section(name):
    global y
    y-=7
    text(name,10,bold=True,color='#171719',gap=5)

def header(zh=False):
    global y,lang
    lang='zh' if zh else 'en'
    c.setFillColor(HexColor('#171719'))
    c.setFont('ChineseBold' if zh else 'SansBold',27 if zh else 25)
    c.drawString(LEFT,H-66,'王泽' if zh else 'Winston (Ze) Wang')
    c.setFont('Sans',10)
    c.setFillColor(HexColor('#626267'))
    c.drawString(LEFT,H-86,'Winston (Ze) Wang' if zh else 'Doctoral Researcher in Engineering')
    if zh:
        c.setFont('Chinese',9.5)
        c.drawString(LEFT,H-103,'工程博士研究生 | 马来西亚吉隆坡')
    else:
        c.drawString(LEFT,H-103,'Kuala Lumpur, Malaysia')
    c.setFont('Sans',9)
    c.drawString(LEFT,H-120,'wangze_phd@163.com  |  +86 17602259373')
    c.linkURL('mailto:wangze_phd@163.com',(LEFT,H-122,LEFT+155,H-111))
    c.drawImage(ImageReader(str(ROOT/'assets/img/prof_pic.jpg')),W-124,H-126,80,80,preserveAspectRatio=True,anchor='c',mask='auto')
    c.setStrokeColor(HexColor('#d9d9dd'))
    c.setLineWidth(.5)
    c.line(LEFT,H-142,W-LEFT,H-142)
    y=H-155

def footer():
    assert y>36, f'Page overflow: {lang}, bottom={y}'
    c.setFillColor(HexColor('#77777c'))
    c.setFont('Sans',7.5)
    c.drawString(LEFT,23,'winstonwang111.github.io  |  ORCID 0000-0003-2955-9206')
    c.linkURL('https://winstonwang111.github.io',(LEFT,20,LEFT+135,31))
    c.linkURL('https://orcid.org/0000-0003-2955-9206',(LEFT+140,20,LEFT+325,31))
    c.drawString(LEFT,36,'Google Scholar  /  LinkedIn')
    c.linkURL('https://scholar.google.com/citations?user=mxKUnH8AAAAJ',(LEFT,34,LEFT+61,43))
    c.linkURL('https://www.linkedin.com/in/winston-wang-065a472a9/',(LEFT+65,34,LEFT+110,43))
    c.drawRightString(W-LEFT,23,'EN / 01' if lang=='en' else 'CN / 02')
    print(lang,'bottom',round(y,1))
    c.showPage()

pubs=[
('Wang, Z.; Qi, G. (2021). Modeling and Analysis of a Three-Terminal-Memristor-Based Conservative Chaotic System.','Entropy 23(1), 71.','https://doi.org/10.3390/e23010071'),
('Hu, J.; Qi, G.; Wang, Z.; Chen, G. (2021). Rare Energy-Conservative Attractors on Global Invariant Hypersurfaces and Their Multistability.','International Journal of Bifurcation and Chaos 31(3), 2130007.','https://doi.org/10.1142/S021812742130007X'),
('Zhang, S.; Wang, Z.; Ma, D. (2021). Simulation and optimization of Flexsim shirt assembly line based on improved ant colony algorithm.','Journal of Textile Research 42(3), 155-160.','https://doi.org/10.13475/j.fzxb.20200700606'),
('Qi, G.; Hu, J.; Wang, Z. (2020). Modeling of a Hamiltonian conservative chaotic system and its mechanism routes from periodic to quasiperiodic, chaos and strong chaos.','Applied Mathematical Modelling 78, 350-365.','https://doi.org/10.1016/j.apm.2019.08.023')]

header()
text('Researcher in nonlinear dynamics and intelligent systems, with experience in conservative chaos, energy-based analysis, numerical modeling, and banking risk assessment.',9.2,gap=2)
section('EDUCATION')
text('Taylor\'s University | Doctoral degree in Engineering, in progress',9.4,True,gap=1)
text('2023-10 - Present | Expected graduation: 2027-10<br/>High-dimensional conservative chaos; energy analysis; reinforcement learning; chaotic dynamics in LLM neural networks.',8.7,gap=4)
text('Tiangong University | Master\'s, Control Science and Engineering',9.4,True,gap=1)
text('2018-09 - 2021-03 | Conservative chaotic system modeling and energy analysis. GPA: 3.38.<br/>Thesis: Analysis and circuit implementation of a conservative chaotic system based on a three-terminal memristor.',8.7,gap=4)
text('Tiangong University | Bachelor\'s, Automation',9.4,True,gap=1)
text('2014-09 - 2018-06 | Automation and control systems. GPA: 2.72.',8.7,gap=2)
section('PROFESSIONAL EXPERIENCE')
text('Industrial Bank Co., Ltd. | 2021-12 - 2023-06',9.4,True,gap=2)
text('Assessed individual and corporate customer risks; applied robotic process automation (RPA) to banking workflows; introduced satellite imagery and related technologies for post-loan monitoring of agricultural, photovoltaic, and wind-power projects.',8.9,gap=2)
section('EARLY INDUSTRY EXPERIENCE')
text('Huadian Inner Mongolia Energy, Tumed Power Generation Branch | 2018-10 - 2018-11<br/>Operations and maintenance internship: plant monitoring, emergency repair participation, and PLC control-system maintenance.',8.7,gap=3)
text('Industrial site visits, Luoyang | 2013-05 - 2013-06<br/>LYC, YTO, CRRC, and diesel-engine facilities; exposure to production lines, standardized operations, and information management.',8.7,gap=2)
section('RESEARCH &amp; PUBLICATIONS')
text('Participated in the project on mechanical analysis, control, and applications of generalized rigid-body chaotic systems (Grant 61873186), and chaos/nonlinear-dynamics conferences in 2019 and 2020.',8.7,gap=4)
for title,venue,url in pubs:
    text(f'<link href="{url}" color="#303033">{escape(title)}</link> <i>{escape(venue)}</i>',8.1,gap=4)
section('TOOLS &amp; QUALIFICATIONS')
text('MATLAB, Altium Designer, Multisim, FlexSim, Microsoft Office; numerical simulation, mathematical modeling, circuit implementation, RPA, and satellite imagery.<br/>National English Competition for College Students, Category C: Second Prize; CET-4; National Computer Rank Examination, Level 2; 2019-2020 academic scholarship (third tier).',8.7,gap=2)
section('RESEARCH OUTLOOK')
text('Investigating energy and chaos in large language models; exploring energy, momentum, and manifold geometry as potential routes to model optimization.',8.9,gap=0)
footer()

header(True)
text('从事非线性动力学与智能系统交叉研究，具有保守混沌、能量分析、数值建模与银行风险评估经验。',9.5,gap=3)
section('教育背景')
text('泰莱大学 | 工程博士在读',10,True,gap=1)
text('2023-10 - 至今 | 预计毕业：2027-10<br/>高维保守混沌建模与能量分析、强化学习，以及大语言模型神经网络中的混沌现象。',9,gap=5)
text('天津工业大学 | 控制科学与工程硕士',10,True,gap=1)
text('2018-09 - 2021-03 | 保守混沌系统建模与能量分析；GPA：3.38。<br/>硕士论文：基于三端忆阻器的保守混沌系统分析与电路实现。',9,gap=5)
text('天津工业大学 | 自动化学士',10,True,gap=1)
text('2014-09 - 2018-06 | 自动化与控制系统；GPA：2.72。',9,gap=3)
section('工作经历')
text('兴业银行 | 2021-12 - 2023-06',10,True,gap=2)
text('评估个人与对公客户风险，以机器人流程自动化（RPA）优化银行业务流程；引入卫星影像等技术，辅助农业、光伏和风电项目的贷后监测与管理。',9.3,gap=3)
section('早期行业经历')
text('华电内蒙古能源有限公司土默特发电分公司 | 2018-10 - 2018-11<br/>运行与检修实习：参与生产监控、应急抢修及PLC控制系统维护。',9,gap=4)
text('洛阳大型国企参访 | 2013-05 - 2013-06<br/>观摩LYC轴承厂、一拖、中车及柴油机厂，学习流水线、标准化作业与信息管理。',9,gap=3)
section('学术研究与论文')
text('参与“广义刚体混沌系统的力学分析、控制与应用”项目（批准号61873186）。<br/>参加2019年与2020年混沌与非线性学术年会。',9,gap=5)
lang='en'
for title,venue,url in pubs:
    text(f'<link href="{url}" color="#303033">{escape(title)}</link> <i>{escape(venue)}</i>',8.1,gap=4)
lang='zh'
section('工具与资格')
text('MATLAB、Altium Designer、Multisim、FlexSim、Microsoft Office；数值仿真、数学建模、电路实现、RPA与卫星影像应用。<br/>全国大学生英语竞赛C类二等奖；大学英语四级（CET-4）；全国计算机等级考试二级；2019-2020学业三等奖学金。',9,gap=3)
section('未来研究方向')
text('深入研究大语言模型的能量与混沌特性，尝试从能量、动量与流形几何的角度探索模型优化的新路径。',9.3,gap=0)
footer()
c.save()
r=PdfReader(TARGET)
assert len(r.pages)==2
doc=pdfium.PdfDocument(str(TARGET))
for i in range(len(doc)):
    doc[i].render(scale=1.65).to_pil().save(OUT/f'cv-preview-{i+1}.png')
print('Created',TARGET)
