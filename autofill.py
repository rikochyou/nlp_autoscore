from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from string import Template
import pandas as pd

# Google Form URL
form_base = 'https://docs.google.com/forms/d/e/1FAIpQLSc6ZKwZWBvtE1po-Xp8vCCJcr2bTWXVqvLea49R8yy_OWDa_g/viewform'

# ===============================
# 以下内容需要根据实际情况修改
# ==============================
csv_path = r"<your csv file path>" # 改为实际csv地址
basic_info = {
    "form_base": form_base,
    "email": "<your email address>", # 改为自己的邮箱
    "sid": "<your student id>", # 改为自己的学号
    "name": "<your name>", # 改为自己的名字
}

# 设置WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = options)

df = pd.read_csv(csv_path)
perform1_trans = {
    1: "There are some important questions about your method, results, or analysis that was not able to resolve.",
    2: "Your presentation was clear about the method, results, and analysis. Any student in the course would have been able to follow.",
    3: "Your presentation was very clear and pedagogic. Even people not in the course would have been able to follow.",
}
perform2_trans = {
    1: "Troublesome. There may be ideas worth salvaging here, but the work should really have been done or evaluated differently.",
    2: "Fairly reasonable work. The approach is not bad, the validation methods are appropriate, and at least the main claims are probably correct.",
    3: "The approach is very appropriate, and the claims are convincingly supported by proper experiments, theoretical analysis or related work.",
}
perform3_trans = {
    1: "Your presentation shows very little understanding of related work.",
    2: "Your presentation shows awareness and understanding of related work.",
    3: "Your presentation shows deep understanding of related work, including research literature.",
}
perform4_trans = {
    1: "Seems thin. There would have been room for significantly more ideas, results, or analysis.",
    2: "Represents an appropriate amount of work for a project in this course.",
    3: "Contains more ideas, results, and analysis than expected for this course.",
}

datalist = []
for _, row in df.iterrows():
    data = {
        "form_base": basic_info["form_base"],
        "email": basic_info["email"],
        "sid": basic_info["sid"],
        "name":basic_info["name"],
        "group": row["group"],
        'mark1':str(row["mark1"]),
        "performance1": perform1_trans.get(row["performance1"], ""),
        "mark2": str(row["mark2"]),
        "performance2": perform2_trans.get(row["performance2"], ""),
        "mark3": str(row["mark3"]),
        "performance3": perform3_trans.get(row["performance3"], ""),
        "mark4": str(row["mark4"]),
        "performance4": perform4_trans.get(row["performance4"], ""),
        "comment": row["comment"] if pd.notnull(row["comment"]) else "",
        # "dlut":"1732696367729",
        }
    datalist.append(data)
for data in datalist:
    form_url_template = "${form_base}?emailAddress=${email}&entry.1939434776=${name}&entry.89701675=${mark1}&entry.481875799=${performance4}&entry.628682245=${mark2} \
    &entry.685734625=${group}&entry.1117921668=${performance1}&entry.1240154713=${mark3}&entry.1332179702=${performance3}&entry.1501265058=${mark4}&entry.1818015541=${sid} \
    &entry.1962655753=${performance2}&entry.918639263=${comment}"
    form_url_init = Template(form_url_template)
    form_url = form_url_init.safe_substitute(data)
    #print(form_url.safe_substitute(data))
    # 打开Google表单
    driver.get(form_url)
    # 等待页面加载完成
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'entry.1939434776')))  # 这是第一个字段ID

    #提交表单
    try:
        time.sleep(30)
        submit_button = driver.find_element(By.CSS_SELECTOR, 'div[role="button"][aria-label="Submit"]')
        submit_button.click()
        time.sleep(2)  # 等待提交成功，避免提交频率过快
    except Exception as e:
            print(f"提交表单时发生错误: {e}")

# 关闭浏览器
driver.quit()

