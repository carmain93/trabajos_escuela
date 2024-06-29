import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:pruebin3/utilis/responsive.dart';

class Welcome extends StatelessWidget {
  const Welcome({super.key});

  @override
  Widget build(BuildContext context) {

     Responsive respon=Responsive.of(context);
    return AspectRatio(
        aspectRatio: 18/11,
      child:  LayoutBuilder(
        builder: (_, constraints){
          return Container(

            child: Stack(
              children: <Widget>[
                Positioned(
                  top: constraints.maxHeight*0.7,
                    child: Column(
                      children: <Widget>[
                        Container(
                          height: 3,
                          width: constraints.maxWidth,
                          color: Color(0xfeeeeeee),
                        ),
                        SizedBox(
                          height: 20,
                        ),
                        Text('Bien, venidos',
                        style: TextStyle(
                          fontSize:20,
                          fontWeight:FontWeight.bold,
                        ),)
                      ],
                    ),

                ),
                Positioned(
                  top: constraints.maxHeight*0,
                    child: SvgPicture.asset('assets/imagenes/pun.svg',
                      height: constraints.maxWidth*0.30,
                    )
                ),

                Positioned(
                    top: constraints.maxHeight*0.20,
                    right: 7,
                    child: SvgPicture.asset('assets/imagenes/kitsu.svg',
                    height: constraints.maxWidth*0.3,
                    )
                )
              ],
            ),
          );
        },
      ),
    );
  }
}
