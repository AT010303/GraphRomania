import tkinter
from tkinter import ttk
from graph import *
from node import node
from pqueue import priorityQueue
from searchalgo import *

space = 1.2

        
def main():
    window = tkinter.Tk()
    window.title("Romania Graph Arad to Bucharest")
    window.geometry("1920x780")


    controls = tkinter.Canvas(window,width=200,height=600)
    controls.pack(side=tkinter.RIGHT)
    Graph = tkinter.Canvas(window,width=900,height=800)


    Exit = tkinter.Button(controls, text='Exit', width=25, command=window.destroy)
    Clr = tkinter.Button(controls,text="Clear screen", width=25, command=lambda:options(Graph,txt_output,0))
    DFS = tkinter.Button(controls, text='DFS', width=25, command=lambda:options(Graph,txt_output,1))
    DLS = tkinter.Button(controls, text='Depthltd 3', width=25, command=lambda:options(Graph,txt_output,2))
    IDDFS = tkinter.Button(controls, text='IDDFS', width=25, command=lambda:options(Graph,txt_output,3))
    BFS = tkinter.Button(controls, text='BestFirst', width=25, command=lambda:options(Graph,txt_output,4))
    Astar = tkinter.Button(controls, text='A*', width=25, command=lambda:options(Graph,txt_output,5))


    Exit.pack(side=tkinter.BOTTOM,pady=2)
    Clr.pack(side=tkinter.BOTTOM,pady=2)
    Astar.pack(side=tkinter.BOTTOM,pady=2)
    BFS.pack(side=tkinter.BOTTOM,pady=2)
    IDDFS.pack(side=tkinter.BOTTOM,pady=2)
    DLS.pack(side=tkinter.BOTTOM,pady=2)
    DFS.pack(side=tkinter.BOTTOM,pady=2)
    
    
    
    
    
    
    txt_output = tkinter.Text(controls, height=50, width=50)
    txt_output.pack(pady=10)
    Graph.pack(side=tkinter.LEFT)
    update(Graph)
    window.mainloop()



def draw_lines(city,Graph):
    map = romania_map.get(city)
    M = list(map.keys())
    x1, y1 = coordinates[city]
    for i in M:
        x2, y2 = coordinates[i]
        Graph.create_line(space*x1, space*y1, space*x2, space*y2)



def draw_nodes(city,Graph):
    X,Y = coordinates[city]
    X = X*space
    Y = Y*space
    Graph.create_rectangle(X-5,Y-5,X+5,Y+5,fill='gray' ,outline = "black", width=2 )
    tkinter.Label(Graph,text=city).place(x=X+20,y=Y-10)


def path_lines(Graph,path):
        for city in range(len(path)-1):
             x1, y1 = coordinates[path[city]]
             x2, y2 = coordinates[path[city+1]]
             Graph.create_line(space*x1, space*y1, space*x2, space*y2,width=10,fill='green')



def options(Graph,text,algo):
    path = []
    Graph.delete('all')
    flg = True
    if algo == 0:
        text.delete("1.0","end")
        update(Graph)
        flg = False
        

    elif algo == 1:
        path = DFS()
        text.insert(tkinter.END,"PATH= "+str(path.path) + "\n")
        text.insert(tkinter.END,"PATH COST= "+str(path.gn) + "\n")
        text.insert(tkinter.END,"DEPTH= "+str(path.Depth) + "\n")
        text.insert(tkinter.END,f"_"*50+"\n")
        flg=True

    elif algo == 2:
        path = DepthLtdS()
        text.insert(tkinter.END,"PATH= "+str(path.path) + "\n")
        text.insert(tkinter.END,"PATH COST= "+str(path.gn) + "\n")
        text.insert(tkinter.END,"DEPTH= "+str(path.Depth) + "\n")
        text.insert(tkinter.END,f"_"*50+"\n")
        flg=True


    elif algo == 3:
        path = IDDFS()
        text.insert(tkinter.END,"PATH= "+str(path.path) + "\n")
        text.insert(tkinter.END,"PATH COST= "+str(path.gn) + "\n")
        text.insert(tkinter.END,"DEPTH= "+str(path.Depth) + "\n")
        text.insert(tkinter.END,f"_"*50+"\n")
        flg=True

    elif algo == 4:
        path = BestFirstSearch()
        text.insert(tkinter.END,"PATH= "+str(path.path) + "\n")
        text.insert(tkinter.END,"PATH COST= "+str(path.gn) + "\n")
        text.insert(tkinter.END,"DEPTH= "+str(path.Depth) + "\n")
        text.insert(tkinter.END,f"_"*50+"\n")
        flg=True

    elif algo == 5:
        path = Astar()
        text.insert(tkinter.END,"PATH= "+str(path.path) + "\n")
        text.insert(tkinter.END,"G(n)/PATH COST= "+str(path.gn)+" " + "H(n)= "+str(path.hn)+" "+"F(n)= "+str(path.fn)+ "\n")
        text.insert(tkinter.END,"DEPTH= "+str(path.Depth) + "\n")
        text.insert(tkinter.END,f"_"*50+"\n")
        flg=True


    if flg == True:   
        path_lines(Graph,path.path)
        update(Graph)

def update(Graph):
    for city in romania_map:
        draw_lines(city,Graph)
    for city in romania_map:
        draw_nodes(city,Graph)
main()