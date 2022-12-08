var
  i,ii:integer;
s:string;
  begin
    write('строка:');
    read(s);
i:=0;
for ii:=1 to length(s)-2 do
  begin
if copy(s,i,3)='aba' then 
  i+=1;
end;
write(i);
  end.