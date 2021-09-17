# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 22:46:40 2016

@author: Gozdem Dural Selcek
"""

import math

'data reading'
data1= [line.strip().split() for line in open('agespecificprevrate.txt')]
data2= [line.strip().split() for line in open('deathrates.txt')]
data3= [line.strip().split() for line in open('popprojfemale.txt')]
data4= [line.strip().split() for line in open('popprojmale.txt')]
data5= [line.strip().split() for line in open('wholesystemrates.txt')]

'time frame'
t=24

'hub caacity'
capacity = 0

'data read: population projections'
M=list()
F=list()

for j in range(0,t):
    MM=list(range(91))
    FF=list(range(91))
    for i in range(0,91):
        MM[i]=float(data4[i][j])
        FF[i]=float(data3[i][j])
    M.append(MM)
    F.append(FF)

'data read: prevalence rates'    
prev=list(range(19))
for i in range(0,19):
    prev[i]=float(data1[0][i])

'data read: death rates' 
DRm=list(range(91))
DRf=list(range(91))
for i in range(0,91):
    DRm[i]=float(data2[i][0])    
    DRf[i]=float(data2[i][1])

'data read: wholesystemrates'
percantagenoneedcc= float(data5[0][0])
yearlyremission= float(data5[1][0])
maxbeddays= float(data5[2][0])
intreadmission=float(data5[4][0])
intreadmissionhub=float(data5[4][1])
intreadmissionthreeplus=float(data5[4][2])

'data read: wholesystemrates-others<3'
admissionperc= float(data5[6][0])
ecpro= float(data5[7][0])
nonecpro= float(data5[8][0])
mmultiplier= list(range(12))
for i in range(0,12):
    mmultiplier[i]= float(data5[9][i])

'data read: wholesystemrates-hub'
admissionperchub= float(data5[11][0])
echubpro= float(data5[12][0])
nonechubpro= float(data5[13][0])
mmultiplierhub= list(range(12))
for i in range(0,12):
    mmultiplierhub[i]= float(data5[14][i])

'data read: wholesystemrates- others 3+'
admissionpercthreeplus= float(data5[16][0])
ecprothreeplus= float(data5[17][0])
nonecprothreeplus= float(data5[18][0])
mmultiplierthreeplus= list(range(12))
for i in range(0,12):
    mmultiplierthreeplus[i]= float(data5[19][i])

'data read: wholesystemrates-readmissions'
readperc=float(data5[21][0])
readperchub=float(data5[22][0])
readpercthreeplus=float(data5[23][0])

'data read: wholesystemrates-LOS'
LOS= float(data5[25][0])
LOShub= float(data5[25][1])
LOSthreeplus= float(data5[25][2])
    
'total population'
totmale=0
TPM=list(range(t))
for j in range(0,t):
    for i in range(0,91):
        totmale=totmale+M[j][i]
    TPM[j]=totmale
    
totfemale=0
TPF=list(range(t))
for j in range(0,t):
    for i in range(0,91):
        totfemale=totfemale+M[j][i]
    TPF[j]=totfemale

TP=list(range(t))
for i in range(0,t):
    TP[i]=TPM[i]+TPF[i]
    

'3+ comorbidity projections'
CPM= list()
CPF= list()
for j in range(0,t):
    cpmm=list(range(91))
    cpff=list(range(91))
    cpp=list(range(91))
    for i in range(0,91):
        z= int(i/5)
        cpmm[i]=math.ceil(M[j][i]*prev[z]*(1-percantagenoneedcc))
        cpff[i]=math.ceil(F[j][i]*prev[z]*(1-percantagenoneedcc))
    CPM.append(cpmm)
    CPF.append(cpff)
    
    
'sex ratio of hub capacity'
SRF=list(range(t))
SRM=list(range(t))
for i in range(0,t):
    SRF[i]=TPF[i]/TP[i]
    SRM[i]=TPM[i]/TP[i]

    
'first year hub population'
HPF=list()
HPM=list()

S=0
fcapacity=math.ceil(capacity*SRF[0])
hpf=list(range(91))
for i in range(0,91):
    if (S<=fcapacity):
        hpf[90-i]=min(max(0,(fcapacity-S)),CPF[0][90-i])
        S=S+hpf[90-i]
        
HPF.append(hpf)


S=0
mcapacity=math.ceil(capacity*SRM[0])
hpm=list(range(91))
for i in range(0,91):
    if (S<=mcapacity):
        hpm[90-i]=min(max(0,(mcapacity-S)),CPM[0][90-i])
        S=S+hpm[90-i]

HPM.append(hpm)


NEWF=list()
WF=list()
NEWM=list()
WM=list()

EC=list()
NONEC=list()
ECHUB=list()
NONECHUB=list()
ECthreeplus=list()
NONECthreeplus=list()

admittedpatient0=list()
admittedpatient1=list()
admittedpatient2=list()
admittedpatient3=list()
admittedpatient4=list()
admittedpatient5=list()
admittedpatient6=list()
admittedpatient7=list()
admittedpatient8=list()
readmittedpatient=list()
readmittedpatienthub=list()
readmittedpatientthreeplus=list()
turndownperc0=list()
turndownperc1=list()
turndownperc2=list()
turndownperc3=list()
turndownperc4=list()
turndownperc5=list()

readmission=intreadmission
readmissionhub=intreadmissionhub
readmissionthreeplus=intreadmissionthreeplus

'''hospital services'''

for j in range(0,t):
      
    'Demand generation from hub'    
    tothubpop=0
    hubdemandmonth=list(range(12))
    ecchub=list(range(12))
    nonecchub=list(range(12))
    for i in range(0,91):
        tothubpop=tothubpop+HPM[j][i]+HPF[j][i]
        hubdemand=tothubpop*admissionperchub
    for i in range(0,12):
        hubdemandmonth[i]=hubdemand*mmultiplierhub[i]
        ecchub[i]=math.ceil(hubdemandmonth[i]*echubpro)
        nonecchub[i]=math.ceil(hubdemandmonth[i]*nonechubpro)
    ECHUB.append(ecchub)
    NONECHUB.append(nonecchub)
    
    'Demand generation from others<3'
    totpop=0
    demand=0
    complexpatient=0
    demandmonth=list(range(12))
    ecc=list(range(12))
    nonecc=list(range(12))
    for i in range(0,91):
        totpop=totpop+M[j][i]+F[j][i]
        complexpatient=complexpatient+CPM[j][i]+CPF[j][i]
    totpop=totpop-complexpatient
    demand=totpop*admissionperc
    for i in range(0,12):
        demandmonth[i]=demand*mmultiplier[i]
        ecc[i]=math.ceil(demandmonth[i]*ecpro)
        nonecc[i]=math.ceil(demandmonth[i]*nonecpro)
    EC.append(ecc)
    NONEC.append(nonecc)

    'Demand generation from others 3+'
   
    demandmonththreeplus=list(range(12))
    eccthreeplus=list(range(12))
    noneccthreeplus=list(range(12))
    totpopthreeplus=complexpatient-tothubpop
    demandthreeplus=totpopthreeplus*admissionpercthreeplus
    for i in range(0,12):
        demandmonththreeplus[i]=demandthreeplus*mmultiplier[i]
        eccthreeplus[i]=math.ceil(demandmonththreeplus[i]*ecprothreeplus)
        noneccthreeplus[i]=math.ceil(demandmonththreeplus[i]*nonecprothreeplus)
    ECthreeplus.append(eccthreeplus)
    NONECthreeplus.append(noneccthreeplus) 
      
    'Bed capacity usage'
    
    admitted0=list(range(12))
    admitted1=list(range(12))
    admitted2=list(range(12))
    admitted3=list(range(12))
    admitted4=list(range(12))
    admitted5=list(range(12))
    read=list(range(12))
    readhub=list(range(12))
    readthreeplus=list(range(12))
    turndown0=list(range(12))
    turndown1=list(range(12))
    turndown2=list(range(12))
    turndown3=list(range(12))
    turndown4=list(range(12))
    turndown5=list(range(12))
    
    for i in range(0,12):        
        read[i]=readmission
        readhub[i]=readmissionhub
        readthreeplus[i]=readmissionthreeplus
        availablecapacity=maxbeddays
        
        if(availablecapacity>0):
            admittedNONECHUB=min(availablecapacity,((nonecchub[i]+readhub[i])*LOShub))
            availablecapacity=availablecapacity-admittedNONECHUB
            admitted0[i]=math.ceil(admittedNONECHUB/LOShub)
        if(admittedNONECHUB<(nonecchub[i]+readhub[i])):
            turndown0[i]=1-(admitted0[i]/(nonecchub[i]+readhub[i]))
            print (j)
            print (availablecapacity)
            print('alarm0')
        else:
            turndown0[i]=0
        if(availablecapacity<=0):
            admitted1[i]=0
            admitted2[i]=0
            admitted3[i]=0
            admitted4[i]=0
            admitted5[i]=0
            turndown1[i]=1
            turndown2[i]=1
            turndown3[i]=1
            turndown4[i]=1
            turndown5[i]=1

        if(availablecapacity>0):
            admittedNONECthreeplus=min(availablecapacity,((noneccthreeplus[i]+readthreeplus[i])*LOSthreeplus))
            availablecapacity=availablecapacity-admittedNONECthreeplus
            admitted1[i]=math.ceil(admittedNONECthreeplus/LOSthreeplus)  
        if(admittedNONECthreeplus<(noneccthreeplus[i]+readthreeplus[i])):
            turndown1[i]=1-(admitted1[i]/(noneccthreeplus[i]+readthreeplus[i]))
            print (j)
            print (availablecapacity)
            print('alarm1')
        else:
            turndown1[i]=0     
        if(availablecapacity<=0):
            admitted2[i]=0
            admitted3[i]=0
            admitted4[i]=0
            admitted5[i]=0
            turndown2[i]=1
            turndown3[i]=1
            turndown4[i]=1
            turndown5[i]=1                      
            
        if(availablecapacity>0):
            admittedNONEC=min(availablecapacity,((nonecc[i]+read[i])*LOS))
            availablecapacity=availablecapacity-admittedNONEC
            admitted2[i]=math.ceil(admittedNONEC/LOS)  
        if(admittedNONEC<(nonecc[i]+readmission)):
            turndown2[i]=1-(admitted2[i]/(nonecc[i]+readmission))
            print (j)
            print (availablecapacity)
            print('alarm2') 
        else:
            turndown2[i]=0        
        if(availablecapacity<=0):
            admitted3[i]=0
            admitted4[i]=0
            admitted5[i]=0
            turndown3[i]=1
            turndown4[i]=1
            turndown5[i]=1
            
        if(availablecapacity>0):
            admittedECHUB=min(availablecapacity,ecchub[i]*LOShub)
            availablecapacity=availablecapacity-admittedECHUB
            admitted3[i]=math.ceil(admittedECHUB/LOShub)
        if(admittedECHUB<ecchub[i]):
            turndown3[i]=1-(admitted3[i]/ecchub[i])
        else:
            turndown3[i]=0
        if(availablecapacity<=0):
            admitted4[i]=0   
            admitted5[i]=0
            turndown4[i]=1
            turndown5[i]=1
            
        if(availablecapacity>0):
            admittedECthreeplus=min(availablecapacity,eccthreeplus[i]*LOSthreeplus)
            availablecapacity=availablecapacity-admittedECthreeplus
            admitted4[i]=math.ceil(admittedECthreeplus/LOSthreeplus)
        if(admittedECthreeplus<eccthreeplus[i]):
            turndown4[i]=1-(admitted4[i]/eccthreeplus[i])
        else:
            turndown4[i]=0
        if(availablecapacity<=0):
            admitted5[i]=0
            turndown5[i]=1
            
        if(availablecapacity>0):
            admittedEC=min(availablecapacity,ecc[i]*LOS)
            availablecapacity=availablecapacity-admittedEC
            admitted5[i]=math.ceil(admittedEC/LOS)
        if(admittedEC<ecc[i]):
            turndown5[i]=1-(admitted5[i]/ecc[i])
        else:
            turndown5[i]=0
         
        readmission=math.ceil((admitted2[i]+admitted5[i])*readperc)
        readmissionhub=math.ceil((admitted0[i]+admitted3[i])*readperchub)
        readmissionthreeplus=math.ceil((admitted1[i]+admitted4[i])*readpercthreeplus)
        
        
        
    admittedpatient0.append(admitted0)
    admittedpatient1.append(admitted1)
    admittedpatient2.append(admitted2)
    admittedpatient3.append(admitted3)
    admittedpatient4.append(admitted4)
    admittedpatient5.append(admitted5)
    readmittedpatient.append(read)
    readmittedpatienthub.append(readhub)
    readmittedpatientthreeplus.append(readthreeplus)        
    turndownperc0.append(turndown0)
    turndownperc1.append(turndown1)
    turndownperc2.append(turndown2)
    turndownperc3.append(turndown3)    
    turndownperc4.append(turndown4)    
    turndownperc5.append(turndown5)    
    
    'aging,deaths,new entrants and waiting list'    
    'FEMALE'
    hpf=list(range(91))
    for i in range(0,89):
        hpf[i+1]=math.ceil(HPF[j][i]*(1-DRf[i])*(1-yearlyremission))
    hpf[90]=math.ceil((HPF[j][89]*(1-DRf[89])+HPF[j][90]*(1-DRf[90]))*(1-yearlyremission))
    S=0
    for i in range(0,91):
        S=S+hpf[i]
    newentrantf=list(range(91))
    waitingf=list(range(91))
    for i in range(0,91):
        if (S<fcapacity):
            newentrantf[90-i]=min((fcapacity-S),max(0,(CPF[j][90-i]-hpf[90-i])))
        else:
            newentrantf[90-i]=0
        S=S+newentrantf[90-i]
        hpf[90-i]=hpf[90-i]+newentrantf[90-i]
        waitingf[90-i]=max(0,(CPF[j][90-i]-hpf[90-i]))
           
    WF.append(waitingf)
    NEWF.append(newentrantf)
    HPF.append(hpf)

    'MALE'
    hpm=list(range(91))
    for i in range(0,89):
        hpm[i+1]=math.ceil(HPM[j][i]*(1-DRm[i])*(1-yearlyremission))
    hpm[90]=math.ceil((HPM[j][89]*(1-DRm[89])+HPM[j][90]*(1-DRm[90]))*(1-yearlyremission))
    S=0
    for i in range(0,91):
        S=S+hpm[i]
    newentrantm=list(range(91))
    waitingm=list(range(91))
    for i in range(0,91):
        if (S<mcapacity):
            newentrantm[90-i]=min((mcapacity-S),max(0,(CPM[j][90-i]-hpm[90-i])))
        else:
            newentrantm[90-i]=0
        S=S+newentrantm[90-i]
        hpm[90-i]=hpm[90-i]+newentrantm[90-i] 
        waitingm[90-i]=max(0,(CPM[j][90-i]-hpm[90-i]))
         
    WM.append(waitingm)
    NEWM.append(newentrantm)
    HPM.append(hpm)
 
 
'Results Display'

'aggregating stock variables by 5yr brackets'
Mag=list()
Fag=list()
CPMag=list()
CPFag=list()
HPMag=list()
HPFag=list()
WMag=list()
WFag=list()
NEWMag=list()
NEWFag=list()
for j in range(0,t):
    Mmag=list(range(19))
    Ffag=list(range(19))
    CPMmag=list(range(19))
    CPFfag=list(range(19))
    HPMmag=list(range(19))
    HPFfag=list(range(19))
    WMmag=list(range(19))
    WFfag=list(range(19))
    NEWMmag=list(range(19))
    NEWFfag=list(range(19))
    for i in range(0,18):
        sum1=0
        sum2=0
        sum3=0
        sum4=0
        sum5=0
        sum6=0
        sum7=0
        sum8=0
        sum9=0
        sum10=0
        for ii in range(0,5):
            sum1=sum1+M[j][i*5+ii]
            sum2=sum2+F[j][i*5+ii]
            sum3=sum3+CPM[j][i*5+ii]
            sum4=sum4+CPF[j][i*5+ii]
            sum5=sum5+HPM[j][i*5+ii]
            sum6=sum6+HPF[j][i*5+ii]
            sum7=sum7+WM[j][i*5+ii]
            sum8=sum8+WF[j][i*5+ii]
            sum9=sum9+NEWM[j][i*5+ii]
            sum10=sum10+NEWF[j][i*5+ii]
        Mmag[i]=sum1
        Ffag[i]=sum2
        CPMmag[i]=sum3
        CPFfag[i]=sum4
        HPMmag[i]=sum5
        HPFfag[i]=sum6
        WMmag[i]=sum7
        WFfag[i]=sum8
        NEWMmag[i]=sum9
        NEWFfag[i]=sum10
    Mmag[18]=M[j][90]
    Ffag[18]=F[j][90]
    CPMmag[18]=CPM[j][90]
    CPFfag[18]=CPF[j][90]
    HPMmag[18]=HPM[j][90]
    HPFfag[18]=HPF[j][90]
    WMmag[18]=WM[j][90]
    WFfag[18]=WF[j][90]
    NEWMmag[18]=NEWM[j][90]
    NEWFfag[18]=NEWF[j][90]
    Mag.append(Mmag)
    Fag.append(Ffag)
    CPMag.append(CPMmag)
    CPFag.append(CPFfag)
    HPMag.append(HPMmag)
    HPFag.append(HPFfag)
    WMag.append(WMmag)
    WFag.append(WFfag)
    NEWMag.append(NEWMmag)
    NEWFag.append(NEWFfag)


'printing results'

outputfile=open('output.txt','w')

for j in range(0,t):
    for i in range(0,19):
        outputfile.write(str(Mag[j][i])+'\t')
    for i in range(0,19):
        outputfile.write(str(Fag[j][i])+'\t')
    for i in range(0,19):
        outputfile.write(str(CPMag[j][i])+'\t')
    for i in range(0,19):
        outputfile.write(str(CPFag[j][i])+'\t')
    for i in range(0,19):
        outputfile.write(str(HPMag[j][i])+'\t')
    for i in range(0,19):
        outputfile.write(str(HPFag[j][i])+'\t')
    for i in range(0,19):
        outputfile.write(str(WMag[j][i])+'\t')
    for i in range(0,19):
        outputfile.write(str(WFag[j][i])+'\t')
    for i in range(0,19):
        outputfile.write(str(NEWMag[j][i])+'\t')
    for i in range(0,19):
        outputfile.write(str(NEWFag[j][i])+'\t')
    for i in range(0,12):
        outputfile.write(str(admittedpatient0[j][i])+'\t')
    for i in range(0,12):
        outputfile.write(str(admittedpatient1[j][i])+'\t')
    for i in range(0,12):
        outputfile.write(str(admittedpatient2[j][i])+'\t')
    for i in range(0,12):
        outputfile.write(str(admittedpatient3[j][i])+'\t')
    for i in range(0,12):
        outputfile.write(str(admittedpatient4[j][i])+'\t')
    for i in range(0,12):
        outputfile.write(str(admittedpatient5[j][i])+'\t')        
    for i in range(0,12):
        outputfile.write(str(turndownperc0[j][i])+'\t')
    for i in range(0,12):
        outputfile.write(str(turndownperc1[j][i])+'\t')
    for i in range(0,12):
        outputfile.write(str(turndownperc2[j][i])+'\t')
    for i in range(0,12):
        outputfile.write(str(turndownperc3[j][i])+'\t')
    for i in range(0,12):
        outputfile.write(str(turndownperc4[j][i])+'\t')
    for i in range(0,12):
        outputfile.write(str(turndownperc5[j][i])+'\t')
    for i in range(0,12):
        outputfile.write(str(readmittedpatient[j][i])+'\t')   
    for i in range(0,12):
        outputfile.write(str(readmittedpatienthub[j][i])+'\t') 
    for i in range(0,12):
        outputfile.write(str(readmittedpatientthreeplus[j][i])+'\t')          


    outputfile.write('\n')   
outputfile.close()
        
        



        
  