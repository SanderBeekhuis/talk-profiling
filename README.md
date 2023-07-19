# Purpose
In this repo I maintain notes about a possible future talk on Performance profiling

# Links
- https://medium.com/@narenandu/profiling-and-visualization-tools-in-python-89a46f578989 
- https://github.com/jrfonseca/gprof2dot
- https://stackoverflow.com/questions/582336/how-do-i-profile-a-python-script
- https://docs.python.org/3/library/profile.html

# Setup
Assuming Python, Ubuntu
```
sudo apt install graphviz
pip install gprof2dot    
```


# Doing a profiling run
```
python -m profile main.py 
gprof2dot -f pstats main.pstats | dot -Tpng -o main.png
```



# Talk structure 
- Number of ways to speed up python code
    - Restrucure
    - Cache
    - Write in C or Cython
- But how to determine what part is slow
    - Easy in 10 line example
    - Hard in the real world
    - We will first look at an example, then to the real world. 

- Basic Profiling
  - Main.py example
- Gprof2dot
    - Pruning options

- Real-World profiling: Printing runtimes at crucial steps
    - In our case we didn't expect the actual block that was slowest
    - Create a test case for the slow part --> This will also help with the later profiling
        - Put it behind a flag to not always run it if it's slow (which it should be) 

# Possible Asides
- Timit
- Memory profiling
- Competitor:  SnakeViz


# TODO
- [ ] Actual calculations in example
  - [ ] Maybe different ways of doing calculations in Pandas
- [ ] Make slides
- [ ] Maybe make workshop?
