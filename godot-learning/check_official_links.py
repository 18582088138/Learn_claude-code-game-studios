"""Check the official pages used by this learning guide; standard library only."""
import concurrent.futures
import json
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

PAGES = {
    "简介": "getting_started/introduction/index.html",
    "基础流程": "getting_started/step_by_step/index.html",
    "节点与场景": "getting_started/step_by_step/nodes_and_scenes.html",
    "创建实例": "getting_started/step_by_step/instancing.html",
    "第一个脚本": "getting_started/step_by_step/scripting_first_script.html",
    "玩家输入": "getting_started/step_by_step/scripting_player_input.html",
    "信号": "getting_started/step_by_step/signals.html",
    "第一款2D游戏": "getting_started/first_2d_game/index.html",
    "项目设置": "getting_started/first_2d_game/01.project_setup.html",
    "玩家场景": "getting_started/first_2d_game/02.player_scene.html",
    "玩家代码": "getting_started/first_2d_game/03.coding_the_player.html",
    "敌人": "getting_started/first_2d_game/04.creating_the_enemy.html",
    "主场景": "getting_started/first_2d_game/05.the_main_game_scene.html",
    "HUD": "getting_started/first_2d_game/06.heads_up_display.html",
    "收尾": "getting_started/first_2d_game/07.finishing-up.html",
    "GDScript基础": "tutorials/scripting/gdscript/gdscript_basics.html",
    "资源": "tutorials/scripting/resources.html",
    "物理简介": "tutorials/physics/physics_introduction.html",
    "Area2D": "tutorials/physics/using_area_2d.html",
    "CharacterBody2D": "tutorials/physics/using_character_body_2d.html",
    "GUI布局": "tutorials/ui/size_and_anchors.html",
    "容器": "tutorials/ui/gui_containers.html",
    "多分辨率": "tutorials/rendering/multiple_resolutions.html",
    "优化概述": "tutorials/performance/general_optimization.html",
    "分析器": "tutorials/scripting/debug/the_profiler.html",
    "存档": "tutorials/io/saving_games.html",
    "Windows导出": "tutorials/export/exporting_for_windows.html",
    "Android导出": "tutorials/export/exporting_for_android.html",
    "iOS导出": "tutorials/export/exporting_for_ios.html",
    "导出教程": "tutorials/export/exporting_projects.html",
    "渲染器": "tutorials/rendering/renderers.html",
    "Timer": "classes/class_timer.html",
    "Camera2D": "classes/class_camera2d.html",
    "TouchScreenButton": "classes/class_touchscreenbutton.html",
    "InputEventScreenTouch": "classes/class_inputeventscreentouch.html",
    "InputEventScreenDrag": "classes/class_inputeventscreendrag.html",
}


class Extractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)

    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data.strip())


def check(item):
    name, path = item
    entry = {"name": name, "path": path}
    for language in ("zh_CN", "en"):
        url = f"https://docs.godotengine.org/{language}/stable/{path}"
        entry[f"url_{language}"] = url
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=25) as response:
                body = response.read().decode("utf-8")
                entry[f"status_{language}"] = response.status
            start = body.find('<div role="main"')
            parser = Extractor()
            parser.feed(body[start:] if start >= 0 else body)
            entry[f"page_title_{language}"] = parser.parts[0] if parser.parts else ""
            if language == "en":
                entry["inspection_excerpt"] = "\n".join(parser.parts)[:3500]
        except Exception as error:
            entry[f"error_{language}"] = str(error)
    return entry


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check, PAGES.items()))
    output = Path(__file__).with_name("official-links.json")
    output.write_text(json.dumps({
        "checked_date": "2026-10-10",
        "note": "官方链接核查与短摘录，不是完整教程副本。stable 会随稳定版更新。",
        "pages": results,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    for entry in results:
        print(entry["path"], entry.get("status_zh_CN", entry.get("error_zh_CN")),
              entry.get("status_en", entry.get("error_en")))
