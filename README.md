# 这是一个自动填写NLP小组pre打分问卷的脚本
1. 请先按照示例nlp_score_sample.csv填写nlp_score_template.csv。
   说明：performance1-4对应问卷中的单选题，一共3个选项，在csv中填整数1、2、3即可。脚本会自动转换为文本
   注意！！！！！！注意！！！！！！！！注意！！！！！！！！！！！！！
   3是最好的评级，1是最差的评级！
   3是最好的评级，1是最差的评级！
   3是最好的评级，1是最差的评级！
   可以理解成3分是最高分，1分是最低分
2. 不需要打分的组在csv中删除对应的行即可
3. 在autofill.py文件中注释里提示需要修改的地方改为实际的信息
4. 代码中的`time.sleep(30)`秒是指30秒后会自动提交表单，如果觉得时间长，可酌情修改。
需要安装这两个包，其他的包看报错提示进行安装
```
pip install selenium
pip install pandas
```
