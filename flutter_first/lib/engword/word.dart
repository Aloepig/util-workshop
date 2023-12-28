import 'package:english_words/english_words.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(WordApp());
}
const help = 1;


class WordApp extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    final wordPair = WordPair.random();
    return MaterialApp(
        home: Scaffold(
          appBar: AppBar(
              title: const Text('하루 하나 영단어')
          ),
          body: Center(
            child: Text(wordPair.asCamelCase),
          ),
        )
    );
    throw UnimplementedError();
  }
}
