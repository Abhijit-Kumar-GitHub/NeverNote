import 'package:flutter/material.dart';
import 'pages/home_page.dart';
import 'pages/auth/register.dart';

void main() => runApp(MaterialApp(
  theme: ThemeData(
    appBarTheme: const AppBarTheme(
      centerTitle: true,
      titleTextStyle:  TextStyle(
        color: Colors.red,
        fontSize: 20.0,
        ),
    )
  ),
  home: const Register(),
));
 
