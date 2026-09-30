import pandas as pd, numpy as np, sys
sys.path.insert(0,'.')
from theme import *
BLUE='#4f46a5'; ORANGE='#175c50'
apply_theme()
s=pd.read_csv('sim_struct.csv')
cols=[(1,1.0),(3,1.0),(1,.6),(3,.6)]
fig,axs=plt.subplots(2,4,figsize=(15,7.6),sharey='row',gridspec_kw=dict(hspace=.62,wspace=.08))
for r,(par,other,ticks,lim) in enumerate([('alpha','gamma_true',[0,.5,1],(-.25,1.9)),('gamma','alpha_true',[0,.3],(-.5,1.1))]):
    for c,(K,cc) in enumerate(cols):
        ax=axs[r,c]; d=s[(s.K==K)&(s.c==cc)]
        lo,hi=ticks[0]-.15,ticks[-1]+.15
        ax.plot([lo,hi],[lo,hi],ls='--',color=GREY,lw=1.2,zorder=1)
        for sc,col,mk,off in [('choice',BLUE,'o',-.03),('rule',ORANGE,'^',.03)]:
            g=d.groupby(par+'_true')[par+'_'+sc]
            m=g.mean(); q1=g.quantile(.025); q2=g.quantile(.975)
            x=m.index.values+off
            ax.vlines(x,q1,q2,color=col,lw=2.2,zorder=3)
            ax.scatter(x,m,color=col,marker=mk,s=70,zorder=4,edgecolor='white',lw=1.3,
                       label='Choice scale' if sc=='choice' else 'Rarity rule')
        ax.set_xticks(ticks); ax.set_xlim(lo,hi); ax.set_ylim(*lim)
        style_axes(ax,grid_axis='y')
        if r==0: ax.set_title(f'K = {K}, c = {cc:g}',loc='center',fontsize=14,fontweight='bold',pad=8)
        ax.set_xlabel(r'true $\alpha$' if par=='alpha' else r'true $\gamma$')
    axs[r,0].set_ylabel(r'estimated $\hat\alpha$' if par=='alpha' else r'estimated $\hat\gamma$')
axs[0,0].legend(loc='upper left',frameon=False,fontsize=12)
fig.text(.085,.955,'A. Opportunity elasticity',fontsize=15,fontweight='bold'); fig.text(.085,.475,'B. Compatibility premium',fontsize=15,fontweight='bold')
fig.savefig('figs/deck_fig_recovery_struct.pdf',bbox_inches='tight'); fig.savefig('figs/deck_fig_recovery_struct.png',dpi=220,bbox_inches='tight')
cell=s.groupby(['alpha_true','gamma_true','c','K'])[['alpha_choice','gamma_choice','kappa_choice','alpha_rule','gamma_rule']].mean().round(3)
cell.to_csv('sim_struct_cells.csv'); print(cell.to_string())
