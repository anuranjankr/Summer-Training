import tensorflow as tf

#define computational graph
#input nodes
X=tf.placeholder(tf.float32,name='x')
Y=tf.placeholder(tf.float32,name='y')
#operation node
addition=tf.add(X,Y,name='addition')
multiply=tf.multiply(X,Y,name='multiply')
subtract=tf.subtract(X,Y,name='Subtraction')

lst=[addition,multiply,subtract]
#create session
with tf.Session() as session:
    #result=session.run(lst[0:3],feed_dict={X:[5,2,1],Y:[10,6,1]})
    result=session.run(addition,feed_dict={X:[5,2,1],Y:[10,6,1]})
    result1=session.run(subtract,feed_dict={X:[5,2,1],Y:[10,6,1]})

    #create an event file in a given directory and add graph to it
    writer=tf.summary.FileWriter('./log', session.graph)
    print(result) 
