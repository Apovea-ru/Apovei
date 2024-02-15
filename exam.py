import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data)
human_robot = data
print(pd.get_dummies(data['whoAmI']))
human_robot.loc[data['whoAmI'] == 'robot', 'robot' ] = '1'
human_robot.loc[data['whoAmI'] == 'human', 'robot' ] = '0'
human_robot.loc[data['whoAmI'] == 'human', 'human' ] = '1'
human_robot.loc[data['whoAmI'] == 'robot', 'human' ] = '0'
human_robot.drop('whoAmI', inplace=True, axis=1)
print(human_robot)

