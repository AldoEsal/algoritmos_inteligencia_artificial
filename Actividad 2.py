import re 
patron=re.compile(r'\W')
 
def profundidad(A,B,C):
      nodos={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7} 
      vi=nodos[B] 
      C=patron.split(C) 
      v1=C[vi]
      Vp=[v1] 
      Ep=[]
      w=v1
      padre={}
      while True:
          while True:
              arista=[(w,x) for x in C if ((w,x) in A and x not in Vp)]
              if arista==[]:
                  break
              vk=arista[0]
              Ep.append(vk)
              Vp.append(vk[1])
              padre.update({vk[1]:w})
              w=vk[1]
          if w==v1:
              print ("Resultado de la busqueda",Ep)
              break
          w=padre.get(w)
         
      return Ep
 
vi='e'
C=('a b c d e f g h')
 
A={('a','b'),('a','c'),('a','g'),('b','a'),('b','d'),('b','g'),('c','a'),('c','d'),('c','e'),
    ('d','b'),('d','c'),('d','f'),('e','c'),('e','f'),('e','g'),('f','d'),('f','e'),('f','h'),
    ('g','a'),('g','b'),('g','e'),('h','f')} 
profundidad(A,vi,C)