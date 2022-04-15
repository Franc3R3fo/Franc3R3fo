#!/usr/bin/env python3

import random, datetime

class Colors:
    COLORS = [
        "lightgreen",
        "green",
        "lightyellow",
        "yellow",
        "orange",
        "lightred",
        "red",
        "lightviolet",
        "violet",
        "lightblue",
        "blue",
        "lightgrey",
        "grey"
    ]
    
    @staticmethod
    def random_color(start=None, end=None):
        if (end == None):
            end = len(Colors.COLORS)
        if (start == None):
            start = 0
        return random.choice(Colors.COLORS[start : end+1])
    
    @staticmethod
    def random_colors(length, start=None, end=None):
        return [ Colors.random_color(start, end) for _ in range(length) ]
    
    @staticmethod
    def sequence_colors(length, start=None):
        if (start == None):
            start = 0
        return Colors.COLORS[start : start+length]

class Badges:
    @staticmethod
    def getZERO(thing, color):
        return f"![{thing}](https://img.shields.io/badge/-{thing}-{color}.svg)"

class Generators:
    @staticmethod
    def getZERO(conf):
        things = conf["things"]
        colors = conf["colors"]
        header = conf["header"]
        return f"\n### {header}\n{' '.join([ Badges.getZERO(thing, color) for (thing, color) in zip(things, colors) ])}\n"
    
    @staticmethod
    def getUNO(conf):
        username = conf["username"]
        header = conf["header"]
        THEME_1 = ""
        THEME_2 = ""
        THEME_2 = ""
        if ("theme_1" in conf):
            THEME_1 = f"&theme={conf['theme_1']}"
        if ("theme_2" in conf):
            THEME_2 = f"&theme={conf['theme_2']}"
        if ("theme_3" in conf):
            THEME_3 = f"&theme={conf['theme_3']}"
        
        HIDE = ""
        if len(conf["hide"])>0:
            HIDE=f"&hide={','.join(conf['hide'])}"
        
        EXCLUDE_REPO = ""
        if len(conf["exclude_repo"])>0:
            EXCLUDE_REPO=f"&exclude_repo={','.join(conf['exclude_repo'])}"
        
        return """\n### """+f"{header}"+"""

<center>
<table>
    <tr>
        """+f"<td><img width=\"500px\" align=\"left\" src=\"https://github-readme-stats.vercel.app/api?username={username}&show_icons=true{THEME_1}\" /></td>"+"""
        """+f"<td><img width=\"450px\" align=\"left\" src=\"https://github-readme-stats.vercel.app/api/top-langs/?username={username}&layout=compact&langs_count=12{THEME_2}{EXCLUDE_REPO}{HIDE}\"/></td>"+"""
    </tr>
    </table>
</center>

<p align="center">

"""+f"![GRAPH](https://activity-graph.herokuapp.com/graph?username={username}&hide_border=true{THEME_3})"+"""

</p>
        """
    @staticmethod
    def getDUE(conf):
        header = conf["header"]
        columns = conf["columns"]
        rows = conf["rows"]
        ss = """\n### """ + f"{header}\n" + "|" + " | ".join(columns) + "|\n" + "|" + " | ".join([ "-"*len(col) for col in columns ]) + "|\n"
        for row in rows:
            ss += "|" + " | ".join([ col for col in row ]) + "|\n"
        return ss
    
    @staticmethod
    def getTRE(conf):
        header = conf["header"]
        username = conf["username"]
        payload = conf["payload"]
        return f"# {username}\n\n" + f"### {header}\n"  + f"{payload}\n"
    
    @staticmethod
    def getWATERMARK():
        return f"\n##### README Credits\nGenerated with windflaag::generate.py on {datetime.date.today()}\n"

config = {
    "BIO": {
        "type": "TRE",
        "username": "windflaag",
        "header": "Bio",
        "payload": """- 👋 Hi, I’m Francesco Refolli
- 👀 I’m interested in Computer Science
- 🌱 I’m currently on 2° Year of Informatica Triennale @ Milano Bicocca
- 💞️ I’m looking to collaborate on Java Class Library in order to add nextChar() in Scanner class"""
    },
    "LANGUAGES": {
        "type": "ZERO",
        "header": "Languages i know",
        "things": ["C", "C++", "JAVA", "PYTHON", "PROLOG", "COMMON%20LISP"],
        "colors": Colors.random_colors(6)
    },
    "OS": {
        "type": "ZERO",
        "header": "OS i prefer",
        "things": ["FEDORA", "ARCH", "DEBIAN", "GENTOO", "SLACKWARE"],
        "colors": Colors.random_colors(5)
    },
    "EDITORS": {
        "type": "ZERO",
        "header": "Editors i use",
        "things": ["NOTEPAD++", "VIM", "GNU%20EMACS", "MICRO"],
        "colors": Colors.random_colors(4)
    },
    "STATISTICS": {
        "header": "My Github statistics",
        "type": "UNO",
        "username": "windflaag",
        "hide": [],
        "exclude_repo": [],
        "theme_1": "tokyonight",
        "theme_2": "tokyonight",
        "theme_3": "redical"
    },
    "CLOSED_PROJECTS": {
        "type": "DUE",
        "header": "Closed projects",
        "columns": ["project", "description", "languages", "close date"],
        "rows": [
            ["nord", "a dialect of lisp with its REPL interpreter", "C++", "27/03/2022"]
        ]
    },
    "ACTIVE_PROJECTS": {
        "type": "DUE",
        "header": "Active projects",
        "columns": ["project", "description", "languages", "current sprint deadline"],
        "rows": [
            ["bignum", "big integer and big double libraries for C++", "C++", "late may 2022"],
            ["concurrency", "experiments about concurrency", "C++", "end april 2022"]
        ]
    },
    "MAINTAINED_PROJECTS": {
        "type": "DUE",
        "header": "Maintained projects",
        "columns": ["project", "description", "languages", "inherited from"],
        "rows": [
            ["pepefetch", "fetcher for unix-like systems", "rust", "[Sigmw](https://github.com/Sigmw)"]
        ]
    },
    "FUTURE_PROJECTS": {
        "type": "DUE",
        "header": "Future projects",
        "columns": ["project", "description", "languages", "sprint starting"],
        "rows": [
            ["caravan", "statistic AI experiments", "C++", "TBD"],
            ["silver", "lisp interpreter", "C++", "TBD"],
            ["panzer", "control version system", "C++", "TBD"]
        ],
    }
}

def main():
    text = ""
    for obj in config:
        if config[obj]["type"] == "ZERO":
            text += Generators.getZERO(config[obj])
        if config[obj]["type"] == "UNO":
            text += Generators.getUNO(config[obj])
        if config[obj]["type"] == "DUE":
            text += Generators.getDUE(config[obj])
        if config[obj]["type"] == "TRE":
            text += Generators.getTRE(config[obj])
    text += Generators.getWATERMARK() # please give me the communist credits for this script
    
    file = open("README.md", "w")
    file.write(text)
    file.close()

main()
