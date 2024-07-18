import 'package:flutter/material.dart';
import 'package:permission_handler/permission_handler.dart';
import 'package:flutter_bluetooth_serial/flutter_bluetooth_serial.dart';
import 'package:after_layout/after_layout.dart';
class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  final _bluetooth= FlutterBluetoothSerial.instance;
  bool BTstate=false;
  bool BTconnected=false;
  BluetoothConnection? connection;
  List<BluetoothDevice> devices=[];
  BluetoothDevice? device;

  @override
  void initState() {
    super.initState();
    permisos();
    estadoBT();
  }
  void permisos() async{
    await Permission.bluetoothConnect.request();
    await Permission.bluetoothScan.request();
    await Permission.bluetooth.request();
    await Permission.location.request();
  }
  void estadoBT(){
    _bluetooth.state.then((value){
      setState(() {
        BTstate=value.isEnabled;
      });
    });
    _bluetooth.onStateChanged().listen((event){
      switch(event){
        case BluetoothState.STATE_ON:
          BTstate=true;
          break;
        case BluetoothState.STATE_OFF:
          BTstate=false;
          break;
        case BluetoothState.STATE_BLE_TURNING_ON:
          break;
        case BluetoothState.STATE_BLE_TURNING_OFF:
          break;

      }
      setState(() {

      });
    });
  }
  void encenderBT()async{
    await _bluetooth.requestEnable();
  }
  void apagarBT()async{await _bluetooth.requestDisable();}

  Widget switchBT(){
    return SwitchListTile(
        title: BTstate? const Text('bluetooth encendido'):const Text('bluetooth apagado') ,
        activeColor:  BTstate?Colors.purple:Colors.grey,
        tileColor:  BTstate?Colors.blue:Colors.grey,
        value: BTstate,
      onChanged: (bool value){
       if(value){
         encenderBT();
       }else{
         apagarBT();
       }
    },
    secondary:  BTstate
      ? const Icon(Icons.bluetooth)
      : const Icon(Icons.bluetooth_disabled),
    );
  }

  Widget inforDisp(){
    return ListTile(
      title: device==null ?Text("Sin dispositivo"):Text("${device?.name}"),
      subtitle: device==null ?Text("Sin dispositivo"):Text("${device?.address}"),
      trailing: BTconnected?IconButton(onPressed: ()=>{

      }, icon: Icon(Icons.delete)):IconButton(onPressed: ()=>{
        listarDisp()
      }, icon: Icon(Icons.search)),
    );
  }
  void listarDisp() async{
    devices = await _bluetooth.getBondedDevices();
    debugPrint(devices[0].name);
    setState(() {

    });
  }
  Widget lista(){
    return devices.isEmpty ? const Text("no hay dispositivos"):
        ListView.builder(
            itemCount: devices.length,
        itemBuilder: (contex, index){
          return ListTile(
            title: Text("${devices[index].name}"),
            subtitle: Text("${devices[index].address}"),
            trailing: IconButton(icon: Icon(Icons.bluetooth_disabled),onPressed: ()async{
              connection = await BluetoothConnection.toAddress(devices[index].address);
              device=devices[index];
              BTconnected=true;
              setState(() {

              });
            },),
          );
        });
  }

  void resisvir_datos(){
   connection?.input?.listen((event)=>{
     contenido = String.fromCharCodes(event)
   });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("flutter <3 bluetod"),),
      body: Column(children: <Widget>[
        switchBT(),
        const Divider(height: 5,),
        inforDisp(),
        Expanded(child: lista())
      ],),
    );
  }


}
