BUFFETT="Life is like a snowball. The important thing is finding wet snow and a really long hill."

echo $BUFFETT | sed -e 's/snow/foot/' -e 's/snow//' -e 's/finding/getting/' -e 's/ wet.*/./g'
