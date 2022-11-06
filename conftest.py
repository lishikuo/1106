#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/10/6 17:11
# @Author  : 李
# @File    : conftest.py.py

import time
import json


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    skipped = terminalreporter.stats.get("skipped", [])
    passed = terminalreporter.stats.get("passed", [])
    failed = terminalreporter.stats.get("failed", [])
    # print("跳过的用例们", skipped)  # 跳过的用例们
    # print("通过的用例们", passed)  # 通过的用例们
    # print("失败的用例们", failed)  # 失败的用例们

    print("跳过的用例数为", len(skipped))
    print("通过的用例数为", len(passed))
    print("失败的用例数为", len(failed))

    """获取失败的用例们的名字"""
    # print("获取失败的用例们", failed)  # 观察发现它是一个list

    failed_name = []
    for i in failed:
        # print(dir(i))  # 用例对象里面的详细引用函数

        """
          #调试代码
          for j in i.__dict__:
              i_data = getattr(i, j)
              print(f"i里面的数据{j}", i_data)
        """
        # print(i.nodeid)

        #print(i.longrepr)#获取错误信息
        _time = time.strftime("%Y-%m-%d %H_%M_%S")  #获取当前时间

        log_path = f'D:/华测项目/testcase/result/{_time}-{i.nodeid.replace("/", "-").replace(".py::", "-").replace("::", "-")}.log'  #存放日志路径
        with open(log_path,"w",encoding="utf-8") as f:
            f.write(str(i.longrepr))

        failed_name.append(i.nodeid)#将错误名称添加到列表
    print(failed_name)

    date = time.strftime("%Y-%m-%d")
    RESULT_PATH = f"D:/华测项目/testcase/result/{date}-result.json"
    result = {}
    if skipped:
        for i in skipped:
            result.update({
                i.nodeid: {
                    "result": "skipped",
                    "date": date
                }
            })

    if passed:
        for i in passed:
            result.update({
                i.nodeid: {
                    "result": "passed",
                    "date": date
                }
            })

    if failed:
        for i in failed:
            result.update({
                i.nodeid: {
                    "result": "failed",
                    "date": date
                }
            })

    open(RESULT_PATH, "w").write(json.dumps(result))


# def pytest_itemcollected(item):
#     print(item.own_markers)  # ⽤例的标签数据 -> 列表




