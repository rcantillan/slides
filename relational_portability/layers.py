import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import LineCollection
from scipy.spatial import Delaunay

IND,GRN,GLD="#302a78","#175c50","#b07d1e"
def base(n=44,seed=5):
    rng=np.random.default_rng(seed)
    pts=[]
    for r in range(7):
        for c in range(9):
            x=c+0.5*(r%2)+rng.normal(0,.18); y=r*0.95+rng.normal(0,.16)
            pts.append((x,y))
    pts=np.array(pts); pts-=pts.mean(0)
    keep=rng.choice(len(pts),n,replace=False)
    return pts[keep]
def edges_local(pos,rng,thr=1.5,p=.85):
    tri=Delaunay(pos); E=set()
    for s in tri.simplices:
        for a,b in ((0,1),(1,2),(0,2)):
            i,j=sorted((s[a],s[b]))
            if np.linalg.norm(pos[i]-pos[j])<thr and rng.random()<p: E.add((i,j))
    return list(E)
def edges_hub(pos,hubs,rng):
    E=set()
    for i in range(len(pos)):
        if i in hubs: continue
        h=sorted(hubs,key=lambda h:np.linalg.norm(pos[i]-pos[h])+rng.normal(0,1.6))[:1]
        for k in h: E.add((min(i,k),max(i,k)))
    for a in hubs:
        for b in hubs:
            if a<b and rng.random()<.6: E.add((a,b))
    return list(E)
def edges_rand(pos,rng,m=48):
    n=len(pos); E=set()
    while len(E)<m:
        i,j=rng.integers(0,n,2)
        if i!=j and np.linalg.norm(pos[i]-pos[j])<3.4: E.add((min(i,j),max(i,j)))
    return list(E)
_K={'k':.40,'sh':.62}
def proj(p,z):
    return np.c_[p[:,0]+_K['sh']*p[:,1], _K['k']*p[:,1]+z]
def render(layers,fname,figsize,gap,title=None,labels=True,dpi=230,bg="#f4f3fb",lpos='right',k=.40,sh=.62,node=230):
    # layers: list of dict(color, edges, big(list), label)
    _K['k']=k; _K['sh']=sh
    pos=base(); n=len(pos)
    fig,ax=plt.subplots(figsize=figsize,dpi=dpi)
    fig.patch.set_facecolor(bg); ax.set_facecolor(bg); ax.axis('off'); ax.set_aspect('equal')
    L=len(layers)
    zs=[(L-1-i)*gap for i in range(L)]       # first layer on top
    W,H=5.6,3.5
    allbig={}
    for lay in layers:
        for b in lay['big']: allbig[b]=lay['color']
    P=[proj(pos,z) for z in zs]
    # draw from bottom plane to top plane
    for idx in reversed(range(L)):
        lay=layers[idx]; z=zs[idx]; col=lay['color']
        corners=np.array([[-W,-H],[W,-H],[W,H],[-W,H]])
        poly=proj(corners,z)
        ax.add_patch(Polygon(poly,closed=True,facecolor=col,alpha=.10,edgecolor='none',zorder=idx*10))
        ax.add_patch(Polygon(poly,closed=True,facecolor='none',edgecolor=col,alpha=.55,linewidth=1.4,zorder=idx*10+1))
        segs=[[P[idx][i],P[idx][j]] for i,j in lay['edges']]
        ax.add_collection(LineCollection(segs,colors=col,linewidths=1.0,alpha=.45,zorder=idx*10+2))
        for i in range(n):
            if i in allbig: continue
            ax.scatter(*P[idx][i],s=22,color='white',edgecolor=col,linewidth=1.0,alpha=.95,zorder=idx*10+3)
        for b,bc in allbig.items():
            mine=(b in lay['big'])
            ax.scatter(*P[idx][b],s=node if mine else 40,color=bc if mine else 'white',edgecolor='white' if mine else bc,linewidth=1.6 if mine else 1.3,zorder=idx*10+4)
        if labels:
            lx=poly[:,0].max()+.15; ly=(poly[1,1]+poly[2,1])/2+.1
            if lpos=='right':
                ax.text(poly[:,0].max()+.3,poly[:,1].mean(),lay['label'],ha='left',va='center',fontsize=lay.get('fs',13),fontweight='bold',color=col)
            else:
                ax.text(poly[3,0]+.1,poly[3,1]+.28,lay['label'],ha='left',va='bottom',fontsize=lay.get('fs',13),fontweight='bold',color=col)
    # interlayer dashed links for the highlighted households
    for b,bc in allbig.items():
        for idx in range(L-1):
            a=P[idx][b]; c=P[idx+1][b]
            ax.plot([a[0],c[0]],[a[1],c[1]],color=bc,linestyle=(0,(2,3)),linewidth=1.4,alpha=.9,zorder=60)
    xs=np.concatenate([proj(np.array([[-W,-H],[W,H],[W,-H],[-W,H]]),z)[:,0] for z in zs])
    ys=np.concatenate([proj(np.array([[-W,-H],[W,H]]),z)[:,1] for z in zs])
    ax.set_xlim(xs.min()-.5,xs.max()+(4.2 if (labels and lpos=='right') else .5)); ax.set_ylim(ys.min()-.4,ys.max()+(1.4 if lpos!='right' else .4))
    if title: ax.text((xs.min()+xs.max())/2,ys.max()+.55,title,ha='center',fontsize=11.5,fontweight='bold',color="#5a5594")
    plt.subplots_adjust(0.005,0.005,0.995,0.995)
    fig.savefig(fname,facecolor=bg,bbox_inches='tight',pad_inches=.15)
    return pos
