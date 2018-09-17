#!/bin/awk -f

BEGIN {


}

{

    theone=0;
    printf("%d",$1);
    j=0;
    for(i=2; i<=NF; i++) {
        if(i%2==0) {
            split($i,a,":");
            theone=(a[2]-1)*12;

        } else {
            split($i,a,":");
            thelinearr[j]=theone+a[2]
            j++;
        }

    }
    slen=asort(thelinearr,tA);
    j=1
    for(i=1;i<=slen;i++){
        for (; j<=tA[i]; j++) {
        if(j==tA[i]) {
            printf(" %d:%d",j,1);
        } else {
            printf(" %d:%d",j,0);
        }
    }
    }
    for(;j<=52; j++) {
        printf(" %d:%d",j,0);
    }
    printf("\n");


}


END{

}
