import load_jiang 
training_data, validation_data, test_data = load_jiang.jiang2("/Users/gaominghui/git/neural-networks-and-deep-learning/data/history.xlsx",5)
import network
net = network.Network([34*5, 20, 34])
net.SGD(training_data, 300, 5, 2.0, test_data=test_data)

