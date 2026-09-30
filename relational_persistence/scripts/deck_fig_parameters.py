import pandas as pd, numpy as np, sys, json
sys.path.insert(0,'.')
from theme import *
BLUE='#4f46a5'; ORANGE='#175c50'
apply_theme()
ds=pd.read_csv('derstandard/ds_struct.csv'); fb=pd.read_csv('fis_struct.csv').set_index('scale').loc['estimated_weights']
fw=json.load(open('fis_fe_wcr_cohort.json'))
FW=dict(alpha=.294,alpha_lo=fw['alpha_set'][0],alpha_hi=fw['alpha_set'][1],gamma=-.257,gamma_lo=fw['gamma_set'][0],gamma_hi=fw['gamma_set'][1])
FC=dict(alpha=.483,alpha_lo=.30,alpha_hi=.85,gamma=-.466,gamma_lo=-.60,gamma_hi=-.25)
lab={'ego_active':'Ego active','both_active':'Both active','new_ties':'New ties','established':'Established ties',
     'low_intensity':'Low reply intensity','high_intensity':'High reply intensity'}
ds['lab']=ds.model.map(lab)
n=len(ds); ys=np.arange(n)[::-1]+2.8; yc=1.8; yw=.8; yb=-.2
fig,axs=plt.subplots(1,2,figsize=(13,6.4),sharey=True,gridspec_kw=dict(wspace=.07))
TOP=n+3.1
bb=dict(facecolor='white',edgecolor='none',pad=1.5)
for ax in axs: ax.axhline(2.3,color=LIGHT_GREY,lw=1); ax.set_ylim(-.8,TOP)
ax=axs[0]
ax.axvline(0,color=GREY,lw=1.2,ls=':',zorder=1); ax.axvline(1,color=GREY,lw=1.2,ls='--',zorder=1)
ax.hlines(ys,ds.alpha_lo,ds.alpha_hi,color=BLUE,lw=2.4,zorder=3); ax.scatter(ds.alpha,ys,color=BLUE,s=75,zorder=4,edgecolor='white',lw=1.5)
ax.hlines(yw,FW['alpha_lo'],FW['alpha_hi'],color=ORANGE,lw=2.4,zorder=3); ax.scatter([FW['alpha']],[yw],color=ORANGE,marker='s',s=75,zorder=4,edgecolor='white',lw=1.5)
ax.hlines(yc,FC['alpha_lo'],FC['alpha_hi'],color=ORANGE,lw=2.4,zorder=3); ax.scatter([FC['alpha']],[yc],color=ORANGE,marker='D',s=70,zorder=4,edgecolor='white',lw=1.5)
ax.text(.5,yb,'not identified between egos',ha='center',va='center',fontsize=11.5,color=GREY,style='italic',bbox=bb,zorder=5)
ax.text(0,n+2.55,'fixed consideration',ha='center',fontsize=11,color=GREY,bbox=bb); ax.text(1,n+2.55,'full-set evaluation',ha='center',fontsize=11,color=GREY,bbox=bb)
ax.set_xlim(-.3,1.3); ax.set_xlabel(r'Opportunity elasticity $\hat\alpha$')
ax.set_yticks(list(ys)+[yc,yw,yb]); ax.set_yticklabels(list(ds.lab)+['Friendship: classmates','Friendship: grade roster','Friendship: between egos'])
ax.set_title('A. Size of the opportunity set',**TITLE_KW); style_axes(ax,grid_axis='x')
ax=axs[1]; XMAX=2.6
ax.axvline(0,color=GREY,lw=1.2,ls=':',zorder=1)
ax.hlines(ys,ds.gamma_lo,ds.gamma_hi,color=BLUE,lw=2.4,zorder=3); ax.scatter(ds.gamma,ys,color=BLUE,s=75,zorder=4,edgecolor='white',lw=1.5)
ax.hlines(yw,FW['gamma_lo'],FW['gamma_hi'],color=ORANGE,lw=2.4,zorder=3); ax.scatter([FW['gamma']],[yw],color=ORANGE,marker='s',s=75,zorder=4,edgecolor='white',lw=1.5)
ax.hlines(yc,FC['gamma_lo'],FC['gamma_hi'],color=ORANGE,lw=2.4,zorder=3); ax.scatter([FC['gamma']],[yc],color=ORANGE,marker='D',s=70,zorder=4,edgecolor='white',lw=1.5)
ax.hlines(yb,fb.gamma_lo,XMAX-.1,color=ORANGE,lw=1.6,ls=(0,(4,2)),zorder=3)
ax.annotate('',xy=(XMAX,yb),xytext=(XMAX-.14,yb),arrowprops=dict(arrowstyle='-|>',color=ORANGE,lw=1.6))
ax.scatter([fb.gamma],[yb],facecolor='white',edgecolor=ORANGE,marker='s',s=75,zorder=4,lw=2)
ax.text(XMAX,yb+.38,'upper limit %.1f'%fb.gamma_hi,ha='right',fontsize=11,color=DARK)
ax.text(0,n+2.55,'pure relative choice',ha='left',fontsize=11,color=GREY,bbox=bb)
ax.set_xlim(-.7,XMAX+.08); ax.set_xlabel(r'Compatibility premium $\hat\gamma$')
ax.set_title('B. Protection beyond choice value',**TITLE_KW); style_axes(ax,grid_axis='x')
fig.savefig('figs/deck_fig_parameters.pdf',bbox_inches='tight'); fig.savefig('figs/deck_fig_parameters.png',dpi=220,bbox_inches='tight')
