from pizza import *
import user_profile

from python.pizza import make_pizza

make_pizza(16,'pepperoni')

make_pizza(12,'mushrooms','green peppers','extra cheese')

user_profile=user_profile.build_progile('albert','einstrin',location='princeton',field='physics')
print(user_profile)
