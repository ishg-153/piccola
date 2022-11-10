import pandas as pd
import matplotlib.pyplot as plt

author=['A','B','C']
article=[1,2,3]
auth_series=pd.Series(author)
article_series=pd.Series(article)
frame={"Author":auth_series,"Article":article_series}
result=pd.DataFrame(frame)
age=[19,20,21]
result["age"]=pd.Series(age)
print(result)
result.plot.bar()
plt.show()