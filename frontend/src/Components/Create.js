import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";

const Create = () => {
    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    // save data
    const [category, setCategory] = useState([]);
    const [formData, SetFormData] = useState({
        name: "",
        category: "",
        slug: "",
        description: "",
        is_active: "",
    });
    const HandelChange = (e) => {
        const { name, value } = e.target;
        SetFormData((Prev) => {
            return { ...Prev, [name]: value };
        });
    };
    const HandleSubmit = (e) => {
        e.preventDefault();
        console.log(formData);

        const interval = setInterval(() => {
            handleClose()
          }, 1000);
          return () => clearInterval(interval);
    };

    return (
        <>
            <div className="row">
                <div className="col mt-3">
                    <Button className="mb-3" variant="primary" onClick={handleShow}>
                        Create post
                    </Button>
                </div>
            </div>

            <Modal show={show} onHide={handleClose} className="modal-lg">
                <Modal.Header closeButton>
                    <Modal.Title>Modal heading</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <div className="container">
                        <form className="submit-post" onSubmit={HandleSubmit}>
                            <h2>Submit your Article</h2>
                            <div className="row">
                                <div className="col-md-6">
                                    <div className="form-group">
                                        <label> Name</label>
                                        <input
                                            type="text"
                                            name="name"
                                            className="form-control"
                                            placeholder=""
                                            onChange={HandelChange}
                                        />
                                    </div>
                                </div>

                                <div className="col-md-6">
                                    <div className="form-group">
                                        <label>Catagory</label>
                                        <select className="form-select" name="category" onChange={HandelChange}>
                                            <option>Catagory</option>
                                            {category.map((Item, index) => {
                                                return (
                                                    <option value={Item.id} key={index}>
                                                        {Item.name}
                                                    </option>
                                                );
                                            })}
                                        </select>
                                    </div>
                                </div>
                            </div>
                            <div className="row">
                                <div className="col-md-6">
                                    <div className="form-group">
                                        <label>Description</label>
                                        <textarea
                                            type="text"
                                            name="description"
                                            className="form-control"
                                            id="description"
                                            placeholder="Description"
                                            onChange={HandelChange}
                                        />
                                    </div>
                                </div>
                                <div className="col-md-6">
                                    <div className="form-group">
                                        <label>Slug</label>
                                        <input
                                            type="text"
                                            name="slug"
                                            className="form-control"
                                            placeholder=""
                                            onChange={HandelChange}
                                        />
                                    </div>
                                </div>
                            </div>
                            <div className="checkbox py-3">
                                <label>
                                    <input
                                        type="checkbox"
                                        name="is_active"
                                        value="1"
                                        id="newsletter"
                                        onChange={HandelChange}
                                    />{" "}
                                    Is Active!
                                </label>
                            </div>
                            <button type="submit" className="btn btn-primary">
                                Submit
                            </button>
                        </form>
                    </div>
                </Modal.Body>
                {/* <Modal.Footer>
                    <Button variant="secondary" onClick={handleClose}>
                        Close
                    </Button>
                    <Button variant="primary" onClick={handleClose}>
                        Save Changes
                    </Button>
                </Modal.Footer> */}
            </Modal>
        </>
    );
};

export default Create;