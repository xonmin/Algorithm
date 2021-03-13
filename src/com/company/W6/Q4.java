public class Q4{
  // 1이 될 때까지
  public void exe(){
    Scanner sc =  new Scanner(System.in);
		int n = sc.nextInt();
		int k = sc.nextInt();
		int count = 0;
		while(true){
			if(n == 1){
				break;
			}
			if(n%k ==0){
				count ++;
				n = n/k;
			}else{
			n -=1;
			count++;
			}
		}
		System.out.println(count);
  }
  
}
