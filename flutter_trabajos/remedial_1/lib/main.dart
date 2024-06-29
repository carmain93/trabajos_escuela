/*
import 'package:flutter/material.dart';

import 'utilis/app.dart';

void main() {
  runApp(const App());
}*/
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Contact Us Form'),
        ),
        body: Padding(
          padding: const EdgeInsets.all(16.0),
          child: ContactForm(),
        ),
      ),
    );
  }
}

class ContactForm extends StatefulWidget {
  @override
  _ContactFormState createState() => _ContactFormState();
}

class _ContactFormState extends State<ContactForm> {
  final _formKey = GlobalKey<FormState>();
  final TextEditingController firstNameController = TextEditingController();
  final TextEditingController lastNameController = TextEditingController();
  final TextEditingController emailController = TextEditingController();
  final TextEditingController messageController = TextEditingController();
  String queryType = 'General Enquiry';
  bool consent = false;

  void _submitForm() {
    if (_formKey.currentState!.validate()) {
      String firstName = firstNameController.text;
      String lastName = lastNameController.text;
      String email = emailController.text;
      String message = messageController.text;

      print('First Name: $firstName');
      print('Last Name: $lastName');
      print('Email: $email');
      print('Query Type: $queryType');
      print('Message: $message');
      print('Consent: $consent');

      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Form submitted successfully')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: ListView(
        children: <Widget>[
          Text(
            'Contact Us',
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
          SizedBox(height: 20),
          TextFormField(
            controller: firstNameController,
            decoration: InputDecoration(
              labelText: 'First Name *',
              border: OutlineInputBorder(),
            ),
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter your first name';
              }
              return null;
            },
          ),
          SizedBox(height: 20),
          TextFormField(
            controller: lastNameController,
            decoration: InputDecoration(
              labelText: 'Last Name *',
              border: OutlineInputBorder(),
            ),
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter your last name';
              }
              return null;
            },
          ),
          SizedBox(height: 20),
          TextFormField(
            controller: emailController,
            decoration: InputDecoration(
              labelText: 'Email Address *',
              border: OutlineInputBorder(),
            ),
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter your email address';
              } else if (!RegExp(r'^[^@]+@[^@]+\.[^@]+').hasMatch(value)) {
                return 'Please enter a valid email address';
              }
              return null;
            },
          ),
          SizedBox(height: 20),
          Text(
            'Query Type *',
            style: TextStyle(fontSize: 16),
          ),
          ListTile(
            title: const Text('General Enquiry'),
            leading: Radio<String>(
              value: 'General Enquiry',
              groupValue: queryType,
              onChanged: (String? value) {
                setState(() {
                  queryType = value!;
                });
              },
            ),
          ),
          ListTile(
            title: const Text('Support Request'),
            leading: Radio<String>(
              value: 'Support Request',
              groupValue: queryType,
              onChanged: (String? value) {
                setState(() {
                  queryType = value!;
                });
              },
            ),
          ),
          TextFormField(
            controller: messageController,
            maxLines: 4,
            decoration: InputDecoration(
              labelText: 'Message *',
              border: OutlineInputBorder(),
            ),
            validator: (value) {
              if (value == null || value.isEmpty) {
                return 'Please enter your message';
              }
              return null;
            },
          ),
          SizedBox(height: 20),
          Row(
            children: <Widget>[
              Checkbox(
                value: consent,
                onChanged: (bool? value) {
                  setState(() {
                    consent = value!;
                  });
                },
              ),
              Expanded(
                child: Text('I consent to being contacted by the team *'),
              ),
            ],
          ),
          SizedBox(height: 20),
          ElevatedButton(
            onPressed: _submitForm,
            child: Text('Submit'),
            style: ElevatedButton.styleFrom(
              padding: EdgeInsets.symmetric(vertical: 16.0),
            ),
          ),
        ],
      ),
    );
  }
}


