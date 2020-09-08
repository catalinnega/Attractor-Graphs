import lorenz.lorenz as lorenz
import rossler.rossler as rossler
import henon.henon as henon

graph_fns = {
        "LOR" : {
            "fn" : lorenz.get_graph
        },
        "ROS" : {
            "fn" : rossler.get_graph
        },
        "HEN" : {
            "fn" : henon.get_graph
        },
}