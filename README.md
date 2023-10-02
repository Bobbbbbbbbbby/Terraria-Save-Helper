# Terraria-Save-Helper
to centralize your terraria saves and load the saves to the right place, and help you start your server

## Protocal Definition
Every command finish in 1 cycle and there are 3 phases in 1 cycle
* Cmd Response
  * Management response
    * 'finised'

There is 2 type of command:
* User command
* Management command
### Phase 1
Phase 1 pass the identity of the sender in the format: `senderType;senderName;senderPassword;`

`senderType` can be `user` and `admin`<br>
`senderName` can be `[userName]` and `manager`<br>
`senderPassword` is set previously

### Phase 2
Phase 2 pass the content of the command in the format: `command:arg`

`command` for `admin`
* `end`

A command can have multiple args in the format: `arg1;arg2;...;argn;`

### Phase 3
Phase 3 is for the server to return value to the client.