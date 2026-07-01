![img.png](img.png)
instance就是Character这个数据库（对象），对象里面有个auther
是个外键，它的数据类型是UserProfile（对象），中键点开它，它有个对象叫user
user里面有个id叫user_id.(user_id=user.id,区别就是下划线id可能少一次数据库查询)