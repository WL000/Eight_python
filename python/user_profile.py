def build_progile(first,last,**user_info):
    profile={}
    profile['first_name']=first;
    profile['last_name']=last;
    for key ,value in user_info.items():
        profile[key]=value
    # 注意return的缩进
    return profile



