/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** summaryRanges(int* nums, int numsSize, int* returnSize) {
	*returnSize=0;
	if(0==numsSize){
		return 0;
	}
	char **ret=malloc(sizeof(char*)*numsSize);
	char buff[265];
	int p1=0;
	int p2=1;
	while(p1<numsSize){
		while(p2<numsSize && nums[p2-1]==nums[p2]-1) ++p2;

		if(p1 < p2-1){
			int isp=sprintf(buff,"%d->%d",nums[p1],nums[p2-1]);
			char *m=malloc(sizeof(char)*(isp+1));
			ret[*returnSize]=strcpy(m,buff);
			++(*returnSize);
		}else{
			int isp=sprintf(buff,"%d",nums[p1]);
			printf("n:%d,isp:%d\n",nums[p1],isp);
			char *m=malloc(sizeof(char)*(isp+1));
			ret[*returnSize]=strcpy(m,buff);
			++(*returnSize);
		}
		p1=p2;
		++p2;
	}
	return ret;
}