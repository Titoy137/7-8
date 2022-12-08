var
  s:string;
  p:integer;
  begin
    write('строка:');
    read(s);
while pos('word',s)>0 do
 begin
  p:=pos('word',s);
  delete(s,p,4);
  insert('letter',s,p);
 end;
 write(s)
 end.