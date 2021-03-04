package com.company.사주차.somastory;

import java.util.ArrayList;
import java.util.List;

public class  Node {

    public Node pre;
    public String data;
    public List<Node> child;

    public Node(String data) { //
        this.data = data;
        this.child = new ArrayList<>();
        this.pre = null;
    }

    public void setChild(Node child) {
        this.child.add(child);
    }

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public List<Node> getChild() {
        return child;
    }

    public Node getPre() {
        return pre;
    }

    public void setPre(Node pre) {
        this.pre = pre;
    }
}
