from locust import TaskSet, HttpLocust

"""1. 定义任务 重点：必须有个形参"""


# 任务1 查询所有学院
def get_all_departments(r):
    # r.client = session对象
    result = r.client.get("/api/departments/")
    print("查询所有学院结果：", result.json())


# 任务2 查询指定学院
def get_one_departments(r):
    result = r.client.get("/api/departments/T06/")
    print("查询指定学院结果：", result.json())


""" 2. 定义任务集 重点：1. 继承TaskSet类  2.组装任务集 tasks = [任务]"""


class TestTask(TaskSet):
    # 相当于 组装测试套件
    tasks = [get_all_departments, get_one_departments]


""" 3. 定义用户行为 重点：1. 继承HttpLocust 2. 使用task_set指定任务集"""


class UserRun(HttpLocust):
    # 必须执行任务集类名
    task_set = TestTask
    host = "http://192.168.38.24:8000"
