;
; BIND data file for local loopback interface
;
$TTL	604800
@	IN	SOA	dev.it-national.com. info.it-national.com. (
			 2014042116	; Serial
			 172800		; Refresh 2 days
			    900		; Retry 15min
			 604800		; Expire 1 week
			   3600 )	; Negative Cache TTL 1hour
;
@	IN	NS	dev.it-national.com.
@	IN	NS	ns.it-national.com.
@	IN	A	81.177.141.232
dev	IN	A	62.75.238.85
ns	IN	A	178.20.232.206
@	IN	MX	10	ns.it-national.com.
@	IN	TXT	"v=spf1 a mx ~all"
mail	IN	A	81.177.141.200
www	IN	A	81.177.141.232
q IN	A	62.75.238.85
1qaz IN	A	62.75.238.85