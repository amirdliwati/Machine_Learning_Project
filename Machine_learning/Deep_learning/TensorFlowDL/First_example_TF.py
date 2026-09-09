import tensorflow as ts

# a = ts.add(3,5)
# sess = ts.Session()
# print(sess.run(a))

var1 = ts.Variable([[1,2],[1,2]], name='Variable1')
var2 = ts.Variable([[3,4],[3,4]], name='Variable2')

result = ts.multiply(var1,var2)
init = ts.global_variables_initializer()

with ts.Session() as sess:
    sess.run(init)
    output = sess.run(result)
    print(output)
    # ts.summary.merge_all() لرسم الجراف
    # ts.summary.FileWriter('Machine_learning/Deep_learning/TensorFlowDL/tensor_Graph',sess._graph)   لرسم الجراف
    
    # tensorboard --logdir Machine_learning/Deep_learning/TensorFlowDL/tensor_Graph  من أجل تشغيل الجراف من الدوز
